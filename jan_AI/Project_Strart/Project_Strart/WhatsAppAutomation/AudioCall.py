from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def WhatsappCall(search,name):
    
    print("Whatsapp Voice Call Automation start: --") 
    click(x=670, y=1050)
    sleep(4)
    write(search)
    press('enter')
    sleep(4)
    click(x=127, y=143)
    sleep(2)
    write(name)
    sleep(2)
    click(x=211, y=225)
    sleep(3)
    click(x=1786, y=101)
    sleep(2)
    click(x=1889, y=24)

WhatsappCall('whatsapp','yashwant')    
