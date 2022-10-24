from django.urls import path
from . import views

urlpatterns = [
    path('',views.cacke_list, name='post_list'),
]