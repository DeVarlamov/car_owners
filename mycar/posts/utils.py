from django.core.paginator import Paginator
from django.conf import settings


def get_page(request, queryset):
    """Пагинация данных по страницам"""
    paginator = Paginator(queryset, settings.COUNT_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
