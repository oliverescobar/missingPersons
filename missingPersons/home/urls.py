from django.urls import path
from .views import HomePageView, indexPageView


urlpatterns = [
    path("", HomePageView, name="home"),
    path("index/", indexPageView, name="index"),
]