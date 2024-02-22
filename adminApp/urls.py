from django.urls import path
from .views import *  # Import the 'index' view function

urlpatterns = [
    path('', index, name='index'), 
    
]