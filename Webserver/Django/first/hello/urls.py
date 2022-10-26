from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name = "index"),
    path("mayur", views.mayur, name = "mayur"),
    path("<str:name>", views.greet, name = "greet")

]