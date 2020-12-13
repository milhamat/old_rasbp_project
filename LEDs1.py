from gpiozero import LED
from time import sleep

led=LED(17)

#while True: membuat menjadi infinite loop
for i in range(5):    
    print(i,'on')
    led.on()
    sleep(1)
    print(i,'off')
    led.off()
    sleep(1)