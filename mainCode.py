import webbrowser
from datetime import datetime
import time
from meetingInfo import meetingList
import pyautogui

isMeetingStarted = False

#Iterate through every sublist in meetingList
for i in meetingList:
    #Infinite loop to check whether the startingTime and System time is same or not
    while True:
        if not isMeetingStarted:
            if datetime.now().hour == int(i[1].split(":")[0]) \
                and datetime.now().minute == int(i[1].split(":")[1]):
                webbrowser.open(i[0])
                isMeetingStarted = True
        elif isMeetingStarted:
            if datetime.now().hour == int(i[2].split(":")[0]) \
                and datetime.now().minute == int(i[2].split(":")[1]):
                pyautogui.keyDown("alt")
                pyautogui.press("q")
                pyautogui.keyUp("alt")
                pyautogui.press("enter")
                isMeetingStarted = False
                break