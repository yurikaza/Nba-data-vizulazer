import pprint
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from flask import Flask, redirect, url_for, render_template, request
from selenium import webdriver
import time
import os
import requests
# Import the pandas library with the usual "pd" shortcut
import pandas as pd


url = "https://nba-player-individual-stats.p.rapidapi.com/players/team"

teamName = 'Sacramento'

querystring = {"name": f'{teamName}'}

headers = {
    'x-rapidapi-key': "a326891b98msh6c30a5f7267e49dp1aa8ecjsna0da69784a3f",
    'x-rapidapi-host': "nba-player-individual-stats.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

dataName = json.loads(response.text)

pprint.pprint(dataName)

#pprint.pprint(dataName)