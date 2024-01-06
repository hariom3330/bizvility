from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('social-auth/',include('social_django.urls',namespace='social-auth'))
]




# serve  static file
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

      # serve media file
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
