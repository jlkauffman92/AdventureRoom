from markupsafe import escape
from classes import *
from subprocess import call
from time import sleep
import sys

def thinking(times, interval):
    i = times
    dots = "."
    while i > 0:
        sys.stdout.write(f"\r {dots}")
        sleep(interval) 
        dots = "." + dots
        i = i-1
    call('clear')

def parseInput(inputText, scene):
    if "look at" in inputText:
        itemName = inputText.split("at ",1)[1]
        for item in scene.items:
            if item.name == itemName:
                current_view = item.lookAt()
                break
            elif item.name == scene.items[-1].name:
                current_view = f"{itemName} doesn't exist"
    else:
        current_view = f'"{inputText}": unknown command. Try again. {scene.description}'
    return scene, current_view

