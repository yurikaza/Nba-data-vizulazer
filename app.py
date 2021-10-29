from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from flask import Flask, redirect, url_for, render_template, request
from dotenv import load_dotenv
import os
import requests


app = Flask(__name__)
load_dotenv()

API_ID = os.getenv("API_ID")
API_SECRET = os.getenv("API_SECRET")

@app.route("/")
def rende_home_page():
        
    try:
            return render_template('index.html')

            if __name__ == '__main__':
                app.run()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


@app.route("/teams", methods=["POST", "GET"])
def rende_team_page():
        
    try:
        if request.method == "POST":

            url = "https://nba-player-individual-stats.p.rapidapi.com/players/team"

            team = request.form['team']

            querystring = {"name": f'{team}'}


            headers = {
                 'x-rapidapi-key': API_ID,
                  'x-rapidapi-host': API_SECRET
                  }

            response = requests.request("GET", url, headers=headers, params=querystring)

            dataName = json.loads(response.text)

            return render_template('team.html', len=len(dataName), dataName=dataName)

            if __name__ == '__main__':
                app.run()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
