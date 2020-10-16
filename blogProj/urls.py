
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'EtihasikDunia Admin'
admin.site.site_title = 'EtihasikDunia Admin'
# admin.site.site_url = 'http://coffeehouse.com/'
admin.site.index_title = 'EtihasikDunia Administration'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('blogApp.urls', namespace='blogApp')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)