from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from mainApp.views import index, doctors, register, profile, profile_data, profile_patient, profile_medcard
from mainApp.views import profile_analyse, test
urlpatterns = [
    path('', index),
    path('registration/', register, name='register'),
    path('doctor/', doctors),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('profile/data/', profile_data, name='profile_data'),
    path('profile/patient/', profile_patient, name='profile_patient'),
    path('profile/medcard/', profile_medcard, name='profile_medcard'),
    path('profile/analyse/', profile_analyse, name='profile_analyse'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('test/', test),
    #path('profile/', ),
]