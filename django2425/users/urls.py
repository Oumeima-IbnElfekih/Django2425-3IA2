from django.urls import path
from .views import *

urlpatterns=[
    path('register/',UserCreateView.as_view(),name="register"),
    path('login/',LoginCustomView.as_view(),name="login"),
    path('logout/',LogoutCustomView.as_view(),name="logout"),
]