from django.urls import path

from . import views

# home directly, goes to views.index with name index
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("<int:id>", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    
]