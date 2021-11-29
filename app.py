from flask import Flask
from flask import render_template
from flask import request
from classes import *
from adventureroom import *
import data

app = Flask(__name__)

@app.route("/")

def start():
    # Data


    #start of program
    return render_template("start.html", scene = data.S1, current_view = data.S1.description)
    # read = str(input("What do you do? (use \"look at <item>\" to see item description) \n")).lower()
    # parseInput(read, s1)

@app.route("/parse-action", methods=['GET','POST'])
def parseAction():
    action = request.args['action']
    scene_id = request.args['scene']
    
    scene = data.SCENES[int(scene_id) - 1]

    new_scene, new_view = parseInput(action, scene)

    return render_template("start.html", scene = new_scene, current_view = new_view)