from django.urls import path
# ("/", .as_view(), name="")

from .views import indexPageView

urlpatterns = [
    path("", indexPageView, name="index")
]