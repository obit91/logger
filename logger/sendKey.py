####################################################
# FILE : sendKey.py
# WRITER : Ohad_Beltzer , oBit91
# DESCRIPTION : sends a message upon call.
####################################################

import pyautogui
# import time
# from multiprocessing import Process


def key_press(input_key):

    filename = "logger.txt"
    with open(filename, "a+") as file:
        file.write(str(input_key))

    # msg = pyautogui.typewrite
    # send_msg = pyautogui.keyDown
    # for i in range(15):
    #     msg("Trololololo number: " + str(i + 1))
    #     send_msg("Enter")
#
# if __name__ == '__main__':
#         p = Process(target=key_press)
#         p.start()
#         p.join()

