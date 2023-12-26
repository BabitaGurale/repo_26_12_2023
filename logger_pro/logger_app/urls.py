from django.urls import path
from .views import personview

urlpatterns = [
    path('person/', personview)
]