from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()

button_sound ={
    Button(17): Sound("samples/drum_tom_mid_hard.wav"),
    
    }
for button, sound in button_sound.items():
    button.when_pressed = sound.play
    
pause()