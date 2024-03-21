from django.contrib import admin
from django.urls import path
from myapp.views import index, toggle, control_servo,pump_run
from myapp.views import index, toggle, control_servo, temperature_data,get_ph_value

urlpatterns = [
    path('', index, name='index'),
    path('<int:led>/', toggle, name='toggle'),
    path('control_servo/', control_servo, name='control_servo'),
    path('WaterPump/',pump_run,name='WaterPump'),
    path('temperature/', temperature_data),
    path('get_ph_value/',get_ph_value, name='get_ph_value'),
    ]