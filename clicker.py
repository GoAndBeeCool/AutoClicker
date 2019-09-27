from pynput.mouse import Button, Controller

from pynput import keyboard

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

# Set pointer position
# Pointer should be a user input but right now is hardcoded
positionX = 145
positionY = 496

break_program = False
def on_press(key):
    global break_program
    print (key)
    if key == keyboard.Key.esc:
        print ('end pressed')
        break_program = True
        return False

with keyboard.Listener(on_press=on_press) as listener:
    while break_program == False:
        mouse.position = (positionX, positionY)
        mouse.press(Button.left)
        mouse.release(Button.left)
    listener.join()
