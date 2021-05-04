
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('khata.urls', namespace='khata')),
    path('api/', include('khata_api.urls', namespace='khata_api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

