import imp
from django.urls import path

from fscohort.views import home

from .views import fscohort, subfolder

urlpatterns = [
    path('', fscohort),
    path('subfolder/', subfolder),
    
]