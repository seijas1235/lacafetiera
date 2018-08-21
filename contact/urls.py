from django.urls import path
from . import views



urlpatterns = [
    #path del contact
    path('', views.contact, name = "contact"),
]