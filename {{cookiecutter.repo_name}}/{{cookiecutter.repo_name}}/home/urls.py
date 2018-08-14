from .views import error, ExampleFormView

from django.urls import path

from django.views.generic.base import TemplateView


urlpatterns = [
    path(r'error/', error, name='error'),
    path(r'', TemplateView.as_view(template_name="index.jinja"), name="home"),
    path(r'form/', ExampleFormView.as_view(), name="Example Form"),
]
