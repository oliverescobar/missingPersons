from django.urls import path
#from .views import indexPageViews
from .views import indexbootstrapPageView
from .views import firstPageView


urlpatterns = [
    path("", indexbootstrapPageView, name="index"),
    path("first/", firstPageView, name="first"),
]