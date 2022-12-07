from django.urls import path
from .views import HomePageView, indexPageView, searchPageView, addpersonPageView


urlpatterns = [
    path("index/", indexPageView, name="index"),
    path("addperson/", addpersonPageView, name="addperson"),
    path("search/", searchPageView, name="search"),
    path("", HomePageView, name="home"),
]
