from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls

urlpatterns = [

    path('', include('posts.urls')),
    path('account/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('inbox/notifications/',
         include(notifications.urls, namespace='notifications')),


]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
