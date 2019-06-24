from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('list_students/', views.list_students, name="list_students"),
    path('ajax_call/', views.ajax_call, name="ajax_call"),
    path('ajax_data/', views.ajax_data, name="ajax_data")
]
