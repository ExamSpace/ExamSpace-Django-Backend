from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/exam/', include('exam.urls')),
    path('api/userInfo/', include('userInfo.urls')),
    path('api/img/',include('img.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)