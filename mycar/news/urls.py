from django.urls import path

from news.views import news_list

app_name = 'news'

urlpatterns = [
    path('news/', news_list, name='news_list'),
]
