from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from myapp.views import index, toggle, control_servo,pump_run

=======
from myapp.views import index, toggle, control_servo, temperature_data
>>>>>>> tem

urlpatterns = [
    path('', index, name='index'),
    path('<int:led>/', toggle, name='toggle'),
    path('control_servo/', control_servo, name='control_servo'),
<<<<<<< HEAD
    path('WaterPump/',pump_run,name='WaterPump')
=======
    path('temperature/', temperature_data)
>>>>>>> tem
]