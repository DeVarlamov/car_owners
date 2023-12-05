from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.cache import cache_page


from posts.forms import CommentForm, PostForm
from .models import Follow, Post, Group, User
from .utils import get_page


@cache_page(20, key_prefix='index_page')
@vary_on_cookie
def index(request):
    """Выводит шаблон главной страницы"""
    post_list = Post.objects.select_related('group', 'author')
    page_obj = get_page(request, post_list)
    return render(request, 'posts/index.html', {"page_obj": page_obj})


def group_posts(request, slug):
    """Выводит шаблон с группами постов"""
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.select_related('author')
    page_obj = get_page(request, post_list)
    return render(request, 'posts/group_list.html', {'group': group,
                                                     'page_obj': page_obj
                                                     })


def profile(request, username):
    """Выводит шаблон профайла пользователя"""
    author = get_object_or_404(User, username=username)
    post = author.posts.all()
    page_obj = get_page(request, post)
    following = (request.user.is_authenticated and author.following.filter(
        user=request.user).exists()
    )
    return render(request, 'posts/profile.html', {
        'page_obj': page_obj,
        'author': author,
        'following': following})


def post_detail(request, post_id):
    """Подробности публикации"""
    post = get_object_or_404(Post, pk=post_id)
    return render(request,
                  'posts/post_detail.html',
                  {'post': post,
                   'form': CommentForm(),
                   'comments': post.comments.all()})


@login_required
def post_create(request):
    """Создания поста"""
    form = PostForm(request.POST or None,
                    files=request.FILES or None,)
    if form.is_valid():
        create_post = form.save(commit=False)
        create_post.author = request.user
        create_post.save()
        return redirect('posts:profile', create_post.author)
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request, post_id):
    """Редактирование поста"""
    edit_post = get_object_or_404(Post, id=post_id)
    if request.user != edit_post.author:
        return redirect('posts:post_detail', post_id)
    form = PostForm(request.POST or None,
                    files=request.FILES or None,
                    instance=edit_post)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post_id)
    return render(request, 'posts/create_post.html', {'form': form,
                                                      'is_edit': True})


@login_required
def add_comment(request, post_id):
    """Модель добавления комментария"""
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post_detail', post_id=post_id)


@login_required
def follow_index(request):
    """информация о текущем пользователе доступна в переменной"""
    posts = Post.objects.filter(author__following__user=request.user)
    page_obj = get_page(request, posts)
    return render(request, 'posts/follow.html', {
        'page_obj': page_obj}
    )


@login_required
def profile_follow(request, username):
    """Подписаться на автора"""
    author = get_object_or_404(User, username=username)
    if author != request.user:
        Follow.objects.get_or_create(user=request.user, author=author)
    return redirect('posts:profile', author)


@login_required
def profile_unfollow(request, username):
    """Дизлайк, отписка"""
    author = get_object_or_404(User, username=username)
    follow = Follow.objects.filter(
        user=request.user,
        author=author
    )
    if follow.exists():
        follow.delete()
    return redirect('posts:profile', username)


@login_required
def delete_post(request, post_id=None):
    '''Удаление поста'''
    post_list = Post.objects.select_related('group', 'author')
    page_obj = get_page(request, post_list)
    post_to_delete = Post.objects.get(id=post_id)
    post_to_delete.delete()
    return render(request, 'posts/index.html', {"page_obj": page_obj})
