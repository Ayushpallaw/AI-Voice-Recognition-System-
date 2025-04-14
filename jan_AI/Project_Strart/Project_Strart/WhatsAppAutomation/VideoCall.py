from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def WhatsappVideo(search,name):
    
    ("Whatsapp VideoCall automation start: --") 
    click(x=670, y=1050)
    sleep(4)
    write(search)
    press('enter')
    sleep(4)
    click(x=127, y=143)
    sleep(4)
    write(name)
    sleep(2)
    click(x=211, y=225)
    sleep(3)
    click(x=1731, y=90)   
    sleep(2)
    click(x=1889, y=24)  

WhatsappVideo('whatsapp', 'yashwant') 