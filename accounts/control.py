import RPi.GPIO as GPIO
from time import *
import time, math
GPIO.setmode(GPIO.BCM)


def pin_configuration(request):
    servoPin =3
    pin = 14
    pin1 = 15
    pin2 = 18
    TRIG = 23
    ECHO = 24
    context ={'servoPin':servoPin,'pin':pin,'pin1':pin1,'pin2':pin2,'TRIG':TRIG,'ECHO':ECHO}
    return (request, context)


def servo_1(request,angle):
    servoPIN = 2
    angle_turn = angle
    GPIO.setup(2, GPIO.OUT)
    pwm=GPIO.PWM(2, 50)
    pwm.start(1.5)
    time.sleep(0.5)
    duty = angle_turn / 18 + 2
    GPIO.output(2, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(2, False)
    pwm.ChangeDutyCycle(0)
    
    
def initial_servo(request):
    GPIO.setmode(GPIO.BCM)
    servoPIN = 3
    GPIO.setup(3, GPIO.OUT)
    pwm=GPIO.PWM(3, 50)
    pwm.start(1.5)
    time.sleep(1.5)

def led_initial(request):
    pin = 14
    pin1 = 15
    pin2 = 18
    GPIO.setup(pin, GPIO.OUT) 
    GPIO.setup(pin1, GPIO.OUT)  
    GPIO.setup(pin2, GPIO.OUT)  
    GPIO.output(pin, 1)       
    GPIO.output(pin1, 1)       
    GPIO.output(pin2, 1)       

def led_green(request):
    print("LED GREEN")
    pin = 14
    pin1 = 15
    pin2 = 18
    led_initial(request)
    time.sleep(0.5)
    GPIO.output(pin, 0)       # set port/pin value to 1/GPIO.HIGH/True  
    GPIO.output(pin1, 1)       # set port/pin value to 1/GPIO.HIGH/True  
    GPIO.output(pin2, 1)       # set port/pin value to 1/GPIO.HIGH/True  
    time.sleep(0.5)
    
def led_red(request):
    print("LED RED")
    pin = 14
    pin1 = 15
    pin2 = 18
    led_initial(request)
    time.sleep(0.5)
    GPIO.output(pin, 1)       # set port/pin value to 1/GPIO.HIGH/True  
    GPIO.output(pin1, 0)       # set port/pin value to 1/GPIO.HIGH/True  
    GPIO.output(pin2, 1)       # set port/pin value to 1/GPIO.HIGH/True  
    time.sleep(0.5)
    
def led_yellow(request):
    print("LED yellow")
    pin = 14
    pin1 = 15
    pin2 = 18
    led_initial(request)
    time.sleep(0.5)
    GPIO.output(pin, 1)       # set port/pin value to 1/GPIO.HIGH/True  
    GPIO.output(pin1, 1)       # set port/pin value to 1/GPIO.HIGH/True  
    GPIO.output(pin2, 0)       # set port/pin value to 1/GPIO.HIGH/True  
    time.sleep(0.5)
    
    

def ultrasonic_sensor():
    
    TRIG = 20
    ECHO = 21
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)  
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
        
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
        
    pulse_duration = (pulse_end - pulse_start)
    distance = pulse_duration * 17150
    distance_final = round (distance + 1.15,2)
    time.sleep(0.5)
    # print("Ultrasonic")
        
    return distance_final




def servopass_function(request):
    led_green(request)
    servo_1(request,angle=90)
    # print("GateUP")
    
    distance = ultrasonic_sensor()
    time.sleep(0.5)
    while distance>=30:
        # print (ultrasonic_sensor())
        # print("In disntance <=30")
        distance = ultrasonic_sensor()
        time.sleep(0.5)
        
    while distance<=30:
        # print (ultrasonic_sensor())
        # print("In disntance >=30")
        distance = ultrasonic_sensor()
        time.sleep(0.5)

    led_red(request)    
    servo_1(request,angle=0)
    # print("GateDown")
    
    
def servogate_function(request):
    initial_servo(request)
    # print("Initial Servo")
    led_red(request)
    servo_1(request,angle=0)
    # print("Servo Down")
    
    
def servomanual_function(request):
    led_yellow(request)
    servo_1(request,angle=90)
    # print("GateUp")
    
    distance = ultrasonic_sensor()
    time.sleep(0.5)
    while distance>=30:
        # print (ultrasonic_sensor())
        # print("In disntance <=30")
        distance = ultrasonic_sensor()
        time.sleep(0.5)
        
    while distance<=30:
        # print (ultrasonic_sensor())
        # print("In disntance >=30")
        distance = ultrasonic_sensor()
        time.sleep(0.5)
    led_red(request)    
    servo_1(request,angle=0)
    # print("GateDown")
    