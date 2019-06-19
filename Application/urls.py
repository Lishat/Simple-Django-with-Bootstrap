from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('list_students/', views.list_students, name="list_students")
]
