from django.urls import path
from .views import registrationForm,registrationSuccess

urlpatterns = [
    path('register/',registrationForm,name='register'),
    path('success/',registrationSuccess,name='success'),


    

]