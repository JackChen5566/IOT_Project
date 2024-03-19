from django.contrib import admin
from django.urls import path
from myapp.views import index, toggle, control_servo,pump_run
from myapp.views import index, toggle, control_servo, temperature_data

urlpatterns = [
    path('', index, name='index'),
    path('<int:led>/', toggle, name='toggle'),
    path('control_servo/', control_servo, name='control_servo'),
    path('WaterPump/',pump_run,name='WaterPump'),
    path('temperature/', temperature_data),
    ]