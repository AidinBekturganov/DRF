from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # API Token Management
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Project URLs
    path('admin/', admin.site.urls),
    path('', include('khata.urls', namespace='khata')),
    # User Management
    path('api/user/', include('users.urls', namespace='users')),
    # Blog_API Application
    path('api/', include('khata_api.urls', namespace='khata_api')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
