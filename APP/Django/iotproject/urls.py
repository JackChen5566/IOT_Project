from django.contrib import admin
from django.urls import path
from myapp.views import index, toggle, control_servo

urlpatterns = [
    path('', index, name='index'),
    path('<int:led>/', toggle, name='toggle'),
    path('control_servo/', control_servo, name='control_servo'),
]