####################################################
# FILE : sendKey.py
# WRITER : Ohad_Beltzer , oBit91
# DESCRIPTION : sends a message upon call.
####################################################

import pyautogui
# import time
# from multiprocessing import Process


def key_press():

    msg = pyautogui.typewrite
    send_msg = pyautogui.keyDown
    for i in range(8):
        # time.sleep(1) # delays for 1 seconds
        msg("This is a msg-sending script, msg number: " + str(i + 1))
        send_msg("Enter")
#
# if __name__ == '__main__':
#         p = Process(target=key_press)
#         p.start()
#         p.join()