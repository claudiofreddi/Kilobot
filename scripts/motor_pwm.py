import RPi.GPIO as GPIO
import time

## sudo chown claudio /dev/gpiomem
## sudo chmod g+rw /dev/gpiomem

left_motor_in1 = 24
left_motor_in2 = 23
left_motor_ena = 25

right_motor_in3 = 14
right_motor_in4 = 15
right_motor_enb = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(left_motor_in1, GPIO.OUT)
GPIO.setup(left_motor_in2, GPIO.OUT)
GPIO.setup(left_motor_ena, GPIO.OUT)

GPIO.setup(right_motor_in3, GPIO.OUT)
GPIO.setup(right_motor_in4, GPIO.OUT)
GPIO.setup(right_motor_enb, GPIO.OUT)

pwm_r = GPIO.PWM(left_motor_ena,1000)
pwm_l = GPIO.PWM(right_motor_enb,1000)

pwm_r.start(75)
pwm_l.start(75)

def forward(second):
    print("forward Moving")
    GPIO.output(right_motor_in3, GPIO.HIGH)
    GPIO.output(right_motor_in4,GPIO.LOW)
    GPIO.output(left_motor_in1, GPIO.HIGH)
    GPIO.output(left_motor_in2,GPIO.LOW)
    time.sleep(second)

def reverse(second):
    print("reverse Moving")

def left(second):
    print("left Moving")

def right(second):
    print("right Moving")

def stop():
    print("stop Moving")
    pwm_r.ChangeDutyCycle(0)
    pwm_l.ChangeDutyCycle(0)

def exit():
    GPIO.cleanup()

def main():
    forward(5)
    reverse(2)
    left(2)
    right(2)
    stop()
    exit()

if __name__ == '__main__':
    main()
