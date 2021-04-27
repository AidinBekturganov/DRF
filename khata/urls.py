from django.urls import path
from django.views.generic import TemplateView

app_name = 'khata'

urlpatterns = [
    path('', TemplateView.as_view(template_name="khata/index.html")),
]