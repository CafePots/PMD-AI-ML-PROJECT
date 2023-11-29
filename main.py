#i'm going to start learing about ML/AI on my own via youtube and all of that fun stuff (11-25-23)
#numpy will be used for a majority of the math
#a good portion of this is going to be finding and parsing data to use
import numpy as np
import pyautogui as pag
import subprocess as sp
import cv2 as cv
from pyvirtualdisplay import Display
from ewmh import EWMH
from PIL import ImageGrab
import os, sys, json, math, datetime, time, threading
print('[',datetime.datetime.now(),']','Program is Running...')
#i picked a game that i want to make an ai for, i want to try and make an ai that can play Tunic.
#DOING PMD instead with pyboy
#pyboy is a tool that bas functionality for AI and all that stuff :)
#it only supports gb and gbc rn :(

#set virtual display
with Display():
    screen = np.array(ImageGrab.grab(bbox=(364, 170, 1561, 972)))

#instance the class
ewmh = EWMH()
def getGBAWindowInfo():
    # Get a list of all visible windows
    all_windows = ewmh.getClientList()

    # Define the title or other identifying information of the mGBA window
    mGBA_window_title = "mGBA"

    # Search for the mGBA window in the list of all windows
    for window in all_windows:
        if mGBA_window_title == window.get_wm_name():
            mGBA_window = window
            return mGBA_window
GameName = "PMDRRT.gba"
def runMGBA():
    #mGBA with PMD final decision
    print('[',datetime.datetime.now(),']','Running %s'% (GameName))
    sp.run(['mgba','-7','SL1/PMD-AI-ML-PROJECT/%s'%(GameName)],stdin=sp.PIPE,text=True)
    
#this should swap to mGBA
def swapToMGBA():
    #print(ewmh.getClientList())
    clList = ewmh.getClientList()
    for Window in clList:
        #print("Visible Name:",ewmh.getWmVisibleName(Window),"\nName:",ewmh.getWmName(Window),"\nPID:",ewmh.getWmPid(Window))
        if ewmh.getWmName(Window) == "b'mGBA'":
            ewmh.setActiveWindow(Window)
            ewmh.display.flush()
            pag.moveTo(pag.size/2)
            pag.click(pag.size/2)
            print('[',datetime.datetime.now(),']','%s active'% (GameName))
            break
#defining GBA controls as functions to make it easier to read
#also bc this is kinda rudamentrary it makes it easier to change how they work later when im not being lazy
def up():
    pag.press('up')
def right():
    pag.press('right')
def down():
    pag.press('down')
def left():
    pag.press('left')
def a():
    pag.press('x')
def b():
    pag.press('z')
def start():
    pag.press('enter')
def select():
    pag.press('backspace')
def lTrig():
    pag.press('a')
def rTrig():
    pag.press('s')
#hold key
def holdUp(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('up')
def holdRight(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('right')
def holdDown(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('down')
def holdLeft(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('left')
def holdA(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('x')
def holdB(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('z')
def holdStart(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('enter')
def holdSelect(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('backspace')
def holdLTrig(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('a')
def holdRTrig(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('s')

#test controls
def testController():
    pag.sleep(10)
    with pag.hold('z'):
        pag.press(['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'])
    pag.press(['enter','enter','enter','enter','enter','enter'])

def StartUp():
    
    while (str(ewmh.getWmName(ewmh.getActiveWindow())) != "b'mGBA'"):
        print('waiting for emulator...')
        #print(ewmh.getWmName(ewmh.getActiveWindow()))
        swapToMGBA()
    print('set to mGBA')
    testTrl.start()
    testTrl.join()
    RunGame.join()

#threads
RunGame = threading.Thread(target=runMGBA)
SwapToEmu = threading.Thread(target=swapToMGBA)
startUp = threading.Thread(target=StartUp)
testTrl = threading.Thread(target=testController)

#start threads
RunGame.start()
startUp.start()
#end threads
startUp.join()
RunGame.join()


print('[',datetime.datetime.now(),']','Program Stopped...')


