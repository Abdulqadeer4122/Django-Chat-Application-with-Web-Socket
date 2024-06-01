from django.urls import path
from .views import *
urlpatterns = [
    path('page', home, name='home_page')

]
