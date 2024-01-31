from django.urls import path

from App.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
]