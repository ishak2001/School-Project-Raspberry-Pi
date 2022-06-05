import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#Der Delay Zwischen dem Drehen der Motoren
delay = 0.005


#Setup Für die Lichtsensoren
pin_to_circuit_1 = 7                        #Oben Links
pin_to_circuit_2 = 8                        #Oben Rechts
pin_to_circuit_3 = 9                        #Unten Links
pin_to_circuit_4 = 10                       #Unten Rechts

#Motor 1
A = 41 #Pin
B = 42 #Pin
C = 43 #Pin
D = 54 #Pin

#Motor 2
E = 47 #Pin
F = 48 #Pin
G = 49 #Pin
H = 50 #Pin

#Setup Für Beide Motoren
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(H, GPIO.OUT)

def setup(a,b,c,d):
    GPIO.output(A, a)
    GPIO.output(B, b)
    GPIO.output(C, c)
    GPIO.output(D, d)
    time.sleep(0.001)


def setup2(e,f,g,h):
    GPIO.output(E, e)
    GPIO.output(F, f)
    GPIO.output(G, g)
    GPIO.output(H, h)
    time.sleep(0.001)

def rc_time_1 (pin_to_circuit_1):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit_1, GPIO.OUT)
    GPIO.output(pin_to_circuit_1, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit_1, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit_1) == GPIO.LOW):
        count += 1

    return count + pin_to_circuit_1

def rc_time_2 (pin_to_circuit_2):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit_2, GPIO.OUT)
    GPIO.output(pin_to_circuit_2, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit_2, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit_2) == GPIO.LOW):
        count += 1

    return count + pin_to_circuit_2

def rc_time_3 (pin_to_circuit_3):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit_3, GPIO.OUT)
    GPIO.output(pin_to_circuit_3, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit_3, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit_3) == GPIO.LOW):
        count += 1

    return count + pin_to_circuit_3

def rc_time_4 (pin_to_circuit_4):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit_4, GPIO.OUT)
    GPIO.output(pin_to_circuit_4, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit_4, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit_4) == GPIO.LOW):
        count += 1

    return count + pin_to_circuit_4





#Nach Oben Dreh Funktion
def TopTurn(deg):
    
    full_circle = 510.0
    degree = full_circle/360*deg
    setup(0,0,0,0)

    while degree > 0.0:
        setup(1,0,0,1)
        setup(0,0,0,1)
        setup(0,0,1,1)
        setup(0,0,1,0)
        setup(0,1,1,0)
        setup(0,1,0,0)
        setup(1,1,0,0)
        setup(1,0,0,0)
        degree -= 1

    #Links Motor 1
    
#Nach Rechts Dreh Funktion
def RightTurn(deg):
    
    full_circle = 510.0
    degree = full_circle/360*deg
    setup2(0,0,0,0)

    while degree > 0.0:
        setup2(1,0,0,0)
        setup2(1,1,0,0)
        setup2(0,1,0,0)
        setup2(0,1,1,0)
        setup2(0,0,1,0)
        setup2(0,0,1,1)
        setup2(0,0,0,1)
        setup2(1,0,0,1)
        degree -= 1
    #Rechts Motor 2
        
#Nach Links Dreh Funktion
def LeftTurn(deg):

    full_circle = 510.0
    degree = full_circle/360*deg
    setup2(0,0,0,0)

    while degree > 0.0:
        setup2(1,0,0,1)
        setup2(0,0,0,1)
        setup2(0,0,1,1)
        setup2(0,0,1,0)
        setup2(0,1,1,0)
        setup2(0,1,0,0)
        setup2(1,1,0,0)
        setup2(1,0,0,0)
        degree -= 1

    #Links Motor 2

#Nach Unten Dreh Funktion
def DownTurn(deg):
    
    full_circle = 510.0
    degree = full_circle/360*deg
    setup(0,0,0,0)

    while degree > 0.0:
        setup(1,0,0,0)
        setup(1,1,0,0)
        setup(0,1,0,0)
        setup(0,1,1,0)
        setup(0,0,1,0)
        setup(0,0,1,1)
        setup(0,0,0,1)
        setup(1,0,0,1)
        degree -= 1
    #Rechts Motor 1



try:
    #Die Setup Funktion Callen, damit alles vor dem Loop Gesetuped wird 
    #Also wird alles vorbereitet für die Folgende While schleife           
    setup()           
    # Main loop
    while True:
        #Ausgaben der Lichtverhältnisse Der Lichtsensoren
        print(rc_time_1(pin_to_circuit_1)) 
        print(rc_time_2(pin_to_circuit_2)) 
        print(rc_time_3(pin_to_circuit_3)) 
        print(rc_time_4(pin_to_circuit_4)) 

        Sensor1 = rc_time_1(pin_to_circuit_1)   #Oben Links
        Sensor2 = rc_time_2(pin_to_circuit_2)   #Oben Rechts
        Sensor3 = rc_time_3(pin_to_circuit_3)   #Unten Links
        Sensor4 = rc_time_4(pin_to_circuit_4)   #Unten Rechts
    


        if(Sensor1 >= Sensor3 and Sensor2 >= Sensor4):
            #StepperMotorCode für Nach Oben Drehen
            
            TopTurn(45)
                 
            #Nach Oben Drehen
        if(Sensor2 >= Sensor1 and Sensor4 >= Sensor3):    
            #StepperMotorCode für Nach Nach Rechts Drehen Drehen
            
            RightTurn(45)
            
            #Nach Rechts Drehen
        if(Sensor3 >= Sensor4 and Sensor1 >= Sensor2):
            #StepperMotorCode für Nach Nach Links Drehen Drehen
                
            LeftTurn(45)
                
            #Nach Links Drehen
        if(Sensor4 >= Sensor2 and Sensor3 >= Sensor1):    
            #StepperMotorCode für Nach Nach Unten Drehen Drehen
            
            DownTurn(45)

            #Nach Unten Drehen
        if(Sensor1 == 0 and Sensor2 == 0 and Sensor3 == 0 and Sensor4 == 0):
            
            print("Alle Sensoren bekommen kein Licht")
            #Es passiert garnichts wenn Alle werte 0 Sind
        
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()