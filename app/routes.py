from app import app
from app.gridgeneration import *
from flask import render_template, flash, redirect, url_for

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/grid")
def grid():
    grids = [initialiseGrid(height=5,width=5,startalivechance=0.4)]
    for x in range(0, app.config["NUMBER_OF_STEPS"]):
        grids.append(simulateStep(grids[x]))
    return render_template("grid.html", grids = grids)
