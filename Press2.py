#program menyalakan LED dengan switch
#saat switch ditekan akan menyebabkan LED menyala
from gpiozero import LED,Button

led=LED(17)
button=Button(2)

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()