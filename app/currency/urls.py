from django.urls import path, include
from .views import UserRequestListView

urlpatterns = [
    path("get-current-usd/", UserRequestListView.as_view(), name="get-current-usd"),
]
