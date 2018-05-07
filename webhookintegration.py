from __future__ import print_function
import requests, json, os, sys
import threading
from flask import Flask, request, render_template, redirect, flash, jsonify, session
app = Flask(__name__)
app.secret_key = 'afdaaf'
url = os.environ['WEBHOOK_URL']

	
def _post(payload):
	r = requests.post(url, data=json.dumps(payload))
	if not _validate_response(r):
		return "Failed"
	flash('You did it!')
	print("Returning OK", file=sys.stdout)
	return "OK"
	
def _validate_response(response):
	if response and response.status_code != 200:
		print("Invalid response. Error = %s" % str(response.body))
		return False
	return True

def post_to_webhook(message):
	payload = {
		'text':message
	}
	return _post(payload)

@app.route('/webhook', methods=['GET'])
def main():
	message = get_current_weather()
	print (message, file=sys.stderr)
	if message:
		post_to_webhook(message)
	return 'Posting message %s' % message

def get_current_weather():
	city_zipcode = "10001"
	slack_msg = None
	weather_app_id = os.environ['WEATHER_APP_KEY']
	weather_url = "http://api.openweathermap.org/data/2.5/weather?zip=%s&units=metric&appid=%s" % (city_zipcode, weather_app_id)
	print ("Url=", weather_url, file=sys.stdout)
	r = requests.get(weather_url)
	json_data = json.loads(r.text)
	city_name = json_data['name']
	current_weather = json_data['weather'][0]['description']
	if city_name and current_weather:
		slack_msg = "Current weather in %s is %s" % (city_name, current_weather)
	return slack_msg

@app.route('/hello', methods=['GET','POST'])
def hello_slash_cmd():
	print ("Inside hello", file=sys.stdout)
	return jsonify(
		parse="full",
        response_type='in_channel',
        text='Random Picture',
		attachments=[
			{
				"image_url":"https://picsum.photos/200/300/?random"	
			}
		]
    )


if __name__ == "__main__":
    app.run(debug=True)
		

    
	
