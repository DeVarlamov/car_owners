from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

handler403 = 'core.views.permission_denied'
handler404 = 'core.views.page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('posts.urls', namespace='posts')),
    path('about/', include('about.urls', namespace='about')),
    path('news/', include('news.urls', namespace='news'))
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
