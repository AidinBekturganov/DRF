from django.urls import path
from .views import CurrentUserView, CustomUserCreate, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('me/', CurrentUserView.as_view(), name="currentuser")
]