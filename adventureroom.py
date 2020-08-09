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
    call('clear')
    if "look at" in inputText:
        itemName = inputText.split("at ",1)[1]
        for item in scene.items:
            if item.name == itemName:
                print(f"{item.lookAt()}")
                break
            elif item.name == scene.items[-1].name:
                print(f"{itemName} doesn't exist")
    elif inputText == "quit" or inputText == "exit":
        print("goodbye!")
        thinking(3, .75)
        sys.exit()
    else:
        print( f"\"{inputText}\": unknown command. Try again.")
    thinking(5, .5)
    print(scene.sceneDescPretty())
    read = str(input("What do you do? (use \"look at <item>\" to see item description) \n")).lower()
    parseInput(read, scene)

# Data
globe = Item("globe", "You can see the whole world!")
chessBoard = Item("chess board", "someone is losing badly")
gun = Weapon("gun", "it shoots", 15)
s1Items = [globe, chessBoard]

s1 = Scene("Scene 1", "You find yourself at a small table. There is a globe and a chess board.", s1Items)

#start of program
print(s1.sceneDescPretty())
read = str(input("What do you do? (use \"look at <item>\" to see item description) \n")).lower()
parseInput(read, s1)

