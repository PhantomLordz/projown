import time
import ctypes

def show_notification(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)

def drink_water_reminder():
    while True:
        show_notification("Drink Water Reminder", "It's time to drink water!")
        time.sleep(1800) 

if __name__ == "__main__":
    drink_water_reminder()