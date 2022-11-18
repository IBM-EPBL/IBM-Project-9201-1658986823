from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import cross_origin
import pandas as pd
import numpy as np
import datetime

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "dRe32OTFMluCZqk6qFtDz95jkqS8FbBK4TrAuw7TgqR4"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__, template_folder="template")

@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("index.html")

@app.route("/predict",methods=['GET', 'POST'])
@cross_origin()
def predict():
	if request.method == "POST":
		# DATE
		date = request.form['date']
		day = float(pd.to_datetime(date, format="%Y-%m-%dT").day)
		month = float(pd.to_datetime(date, format="%Y-%m-%dT").month)
		# MinTemp
		minTemp = (request.form['mintemp'])
		# MaxTemp
		maxTemp = (request.form['maxtemp'])
		# Rainfall
		rainfall = (request.form['rainfall'])
		# Evaporation
		evaporation = (request.form['evaporation'])
		# Sunshine
		sunshine = (request.form['sunshine'])
		# Wind Gust Speed
		windGustSpeed = (request.form['windgustspeed'])
		# Wind Speed 9am
		windSpeed9am = (request.form['windspeed9am'])
		# Wind Speed 3pm
		windSpeed3pm = (request.form['windspeed3pm'])
		# Humidity 9am
		humidity9am =(request.form['humidity9am'])
		# Humidity 3pm
		humidity3pm = (request.form['humidity3pm'])
		# Pressure 9am
		pressure9am = (request.form['pressure9am'])
		# Pressure 3pm
		pressure3pm = (request.form['pressure3pm'])
		# Temperature 9am
		temp9am = (request.form['temp9am'])
		# Temperature 3pm
		temp3pm = (request.form['temp3pm'])
		# Cloud 9am
		cloud9am = (request.form['cloud9am'])
		# Cloud 3pm
		cloud3pm = (request.form['cloud3pm'])
		# Cloud 3pm
		location = (request.form['location'])
		# Wind Dir 9am
		winddDir9am = (request.form['winddir9am'])
		# Wind Dir 3pm
		winddDir3pm = (request.form['winddir3pm'])
		# Wind Gust Dir
		windGustDir = (request.form['windgustdir'])
		# Rain Today
		rainToday = (request.form['raintoday'])
	return render_template("predictor.html")
		
		
	

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [[
                                "f0",
                                "f1",
                                "f2",
                                "f3",
                                "f4",
                                "f5",
                                "f6",
                                "f7",
                                "f8",
                                "f9",
                                "f10",
                                "f11",
                                "f12",
                                "f13",
                                "f14",
                                "f15",
                                "f16"
                        ]], "values":[[15, 25.5, 3.7, 4.2, 9.3, 35, 3, 15, 79, 37, 1012.5, 1008.2, 7, 4, 17.6, 27.7, 3.5]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/9f322f69-cea1-4ccb-9a5c-49ec65275698/predictions?version=2022-11-18', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predict = response_scoring.json()
val = (predict['predictions'][0]['values'][0][0])	
print(val)
if __name__=='__main__':
	app.run(debug=True)