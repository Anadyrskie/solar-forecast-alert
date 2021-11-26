# designed for forecast.solar api

import requests
import sys
from config import *
from twilio.rest import Client
from datetime import datetime
from time import tzname

def main():
    print(now())
    try:
        print("Fetching forecast.solar JSON")
        json = get_JSON(solar_forecast["url"])
        print("Fetched, parsing")
        message = parse_JSON(json, solar_forecast["watts_required"])
        print("Evaluating")
        if message != "":
            message = ("Warning, the following day(s) may have low (<" +
                       str(solar_forecast["watts_required"]) +
                       "Wh) solar harvest:\n" + message)
            print("Sending message")
            send_telegram(message, telegram)
            print("===DONE===\n")
        else:
            print("Adequate solar")
            print("===DONE===\n")
    except Exception as e:
        try: print(now() + str(e))
        except Exception as e2:
            print(e2)


def get_JSON(url):
    response = requests.get(url)
    return response.json()

def post(url, body):
    response = requests.post(url, body)
    return response

def parse_JSON(json, watts_required):
    message = ""
    try:
        #iterates through forecast JSON
        for day in json["result"]["watt_hours_day"]:
            if json["result"]["watt_hours_day"][day] < watts_required:
                message = message + day + ": " + str(json["result"]["watt_hours_day"][day]) + "Wh" +"\n"
    except TypeError as err:
        print("parse_JSON TypeError: " + str(err))
        sys.exit(0)
    return message

def send_telegram(message, telegram):
    url = "https://api.telegram.org/bot" + telegram["api_key"] + "/sendMessage"
    #requests sends dict as urlencoded
    body = {
        "chat_id":  telegram['chat_id'],
        "text"   :  message
    }
    response = post(url, body)
    json = response.json()
    #response check
    if json['ok'] == True: return
    else:
        print("send_telegram response: " +json)
        return

def now():
    now = datetime.now()
    return now.strftime("%Y-%m-%d" + " %H:%M" + tzname[0])


main()