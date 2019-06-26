
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

MATRIX = [[1,2,3,'A'],
     [4,5,6,'B'],
     [7,8,9,'C'],
     ['*',0,'#','D']]

ROW = [26 ,24 , 22 ,18]
COL = [16 ,12 ,10 , 8]

for j in range (4) :
    GPIO.setup(COL[j], GPIO.IN ,pull_up_down = GPIO.PUD_UP)
for j in range (4) :
    GPIO.setup(ROW[j], GPIO.OUT)
    GPIO.output(ROW[j] , 0)
while(True):
        for col in range(4): #check for selected col
            if GPIO.input(COL[col]) == 0:  #col (i) is clicked
                    for j in range (4) :
                        GPIO.output(ROW[j],1)
                        if GPIO.input(COL[col]) == 1 :
                               print (MATRIX[j][col])
                               time.sleep(0.5)
                               GPIO.output(ROW[j],0)
                               col = 0
                               break
                        GPIO.output(ROW[j],0)
