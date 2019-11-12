import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
image_num = 1


while True:
    input_state = GPIO.input(18)
    if input_state == False:
        strImage = str(image_num)
        os.system("raspistill -t 1000 -hf -vf -o /home/pi/image" + strImage + ".jpg")
        image_num = image_num + 1
        time.sleep(0.2)
