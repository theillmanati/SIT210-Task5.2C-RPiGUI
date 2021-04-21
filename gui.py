import tkinter as tk
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# HARDWARE #
redLED = LED(10)
yellowLED = LED(9)
greenLED = LED(11)

# GUI DEFINITIONS #
win = tk.Tk()
win.title("Task 5.2C - Building a GUI")
stdFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

# FUNCTIONS #
def off():
    redLED.off()
    yellowLED.off()
    greenLED.off()
    
def toggleRedLED():
    if redLED.is_lit:
        redLED.off()
    else:
        off() # Makes sure only red is on
        redLED.on()
        
def toggleYellowLED():
    if yellowLED.is_lit:
        yellowLED.off()
    else:
        off() # Makes sure only yellow is on
        yellowLED.on()
        
def toggleGreenLED():
    if greenLED.is_lit:
        greenLED.off()
    else:
        off() # Makes sure only green is on
        greenLED.on()

def close():
    GPIO.cleanup()
    win.destroy()
    
# WIDGET #
buttonRedLED = tk.Button(win, text = "Red LED", font = stdFont, command = toggleRedLED, bg = 'red', height = 1, width = 20)
buttonRedLED.grid(row = 0, column = 1)

buttonYellowLED = tk.Button(win, text = "Yellow LED", font = stdFont, command = toggleYellowLED, bg = 'yellow', height = 1, width = 20)
buttonYellowLED.grid(row = 1, column = 1)

buttonGreenLED = tk.Button(win, text = "Green LED", font = stdFont, command = toggleGreenLED, bg = 'light green', height = 1, width = 20)
buttonGreenLED.grid(row = 2, column = 1)

exitButton = tk.Button(win, text = "Exit", font = stdFont, command = close, height = 1, width = 20)
exitButton.grid(row = 3, column = 1)

win.protocol("WM_DELETE_WINDOW", close) # Closes window cleanly when clicking X in top corner
win.mainloop() # Keep GUI running by looping forever.
