from flask import render_template, redirect

from flask_app import app
from flask_app.models.elect2020model import Election2020

import subprocess


@app.route('/')
def home ():
    election = Election2020.get_all_votes()
    return render_template("Map.html", election = election);


@app.route('/<int:item_id>')
def individualstate(item_id):
    data = {
        "id": item_id
    }
    state = Election2020.get_one_state(data)
    return render_template("State.html", state = state);


@app.route('/clickablemap')
def mapsource():
    return redirect ("https://www.createaclickablemap.com/");


@app.route('/nytimes')
def newyorktimes():
    return redirect ("https://www.nytimes.com/interactive/2020/11/03/us/elections/results-president.html")

@app.route('/amcharts')
def amcharts():
    return redirect("https://www.amcharts.com/visited_states/#")

# attempting to render google charts using MySQL data below:

def php(script_path):
    p = subprocess.Popen(['php', script_path], stdout=subprocess.PIPE)
    result = p.communicate()[0]
    return result

@app.route('/test')
def apidatachart():
    apipage = php("api.php")
    return apipage;