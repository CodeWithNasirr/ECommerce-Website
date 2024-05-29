from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Blog"),
    path("front", views.front, name="Front")

]
