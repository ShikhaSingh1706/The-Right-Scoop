
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')), 
    path('admin/', admin.site.urls),
    path('api/auth/',include('authentication.urls')),
    path('user/', include('user_dashboard.urls')),
    path('category/', include('category.urls')),


]



# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)