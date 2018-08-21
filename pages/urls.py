from django.urls import path
from . import views

urlpatterns = [
    #path del blog
    path('', views.page, name = "pagina"),
    path('<int:page_id>/<slug:page_slug>', views.page, name="page")
]