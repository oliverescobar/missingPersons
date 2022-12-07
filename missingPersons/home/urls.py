from django.urls import path
from .views import HomePageView, indexPageView, searchPageView


urlpatterns = [
    path("", HomePageView, name="home"),
    path("search/", searchPageView, name="search"),
    path("index/", indexPageView, name="index"),
]