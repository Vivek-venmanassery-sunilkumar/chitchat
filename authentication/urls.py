from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', Signup.as_view()),
    path('login/', Login.as_view()),
]
