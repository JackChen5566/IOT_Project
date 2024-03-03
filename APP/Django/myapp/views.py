from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from bottle import route, run
from gpiozero import LED
from gpiozero import AngularServo
from time import sleep

leds = [LED(26), LED(27)]
states = [False, False]


def servo_run():
    servo = AngularServo(17, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0025)
    servo.angle = 180
    sleep(2)
    servo.angle = 0
    sleep(2)

def control_servo(request):
    # Call the servo_run function when the button is clicked
    servo_run()
    return index(request)

def update_leds():
    for i, value in enumerate(states):
        if value:
            leds[i].on()
        else:
            leds[i].off()

def cleanup_gpio():
    for led in leds:
        led.off()

def index(request):
    update_leds()
    return render(request, 'index.html', {'states': states})

def toggle(request, led):
    if 0 <= led <= 1:
        states[led] = not states[led]
        update_leds()
    return index(request)