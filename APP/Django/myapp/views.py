from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from gpiozero import LED
from gpiozero import AngularServo
from time import sleep
from gpiozero import OutputDevice
import mysql.connector
from myapp import test_fk
from django.http import JsonResponse
import serial 

pump = OutputDevice(18)
pump.off()
pumpstate=False

leds = [LED(26), LED(27)]
states = [False, False]

# Database Setup
db_connection = mysql.connector.connect(
    host="192.168.58.7",
    port=8888,
    user="admin",
    password="admin",
    database="led_control"
)
cursor = db_connection.cursor()

def record_led_state(led_number, state):
    cursor.execute('''
        INSERT INTO led_states (led_number, state) VALUES (%s, %s)
    ''', (led_number, int(state)))
    db_connection.commit()

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
    return render(request, 'index.html', {'states': states,'pumpstate': pumpstate})

def toggle(request, led):
    if 0 <= led <= 1:
        states[led] = not states[led]
        update_leds()
        record_led_state(led, states[led])
    return index(request)

def pump_run(request):
    global pumpstate
    pump.toggle()
    pumpstate = not pumpstate
    return index(request)

def temperature_data(request):
    (h,temperature)=test_fk.temperature()
    return render(request, 'index.html', {'temperature': temperature})


def get_ph_value(request):
    port = "/dev/ttyACM0"
    serial_arduino = serial.Serial(port, 9600)
    serial_arduino.flushInput()
    ph_value = float(serial_arduino.readline())
    return JsonResponse({'ph_value': ph_value})
