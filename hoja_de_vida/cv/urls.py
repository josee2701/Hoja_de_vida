from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = "perfil"
urlpatterns = [
    path("", views.TemplatePerfil.as_view(), name="perfil"),
]


