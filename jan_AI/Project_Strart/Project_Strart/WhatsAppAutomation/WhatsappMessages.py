from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def WhatsappMsg(search,name,messages):
    
    print("Whatsapp message automation start: --") 
    click(x=670, y=1050)
    sleep(1)
    write(search)
    press('enter')
    sleep(4)
    click(x=127, y=143)
    sleep(2)
    write(name)
    sleep(2)
    click(x=211, y=225)
    sleep(3)
    click(x=783, y=987)
    write(messages)
    sleep(2)
    click(x=1879, y=988)
    sleep(2)
    click(x=1889, y=24)

WhatsappMsg('whatsapp','yashwant','hii')
        