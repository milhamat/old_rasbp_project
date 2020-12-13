#program saat switc di tekan akan mengakibatkan
#perubahan status 'ditekan'dan 'lepas'
from gpiozero import Button
from time import sleep

button=Button(2)

while True: #infinite
    if button.is_pressed:
        print('di tekan!')
    else:
        print('lepas!')
    sleep(1)