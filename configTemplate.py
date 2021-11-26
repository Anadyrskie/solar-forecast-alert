# designed for forecast.solar api
# script currently imports config.py

solar_forecast = {
    "api_key" : "",
    "lat" : "",
    "long" : "",
    "declination" : "",
    "azimuth" : "",
    "kWpanels" : "",
    # "api_function":"watthours/day/",  #currently unused, see url concatenation
    "watts_required" : 0  # use Int
}
# <editor-fold desc="url concatenation">
solar_forecast["url"] = ("https://api.forecast.solar/" +
                         solar_forecast["api_key"] +
                         "/estimate/" +
                         # solar_forecast["api_function"] +  # parse_JSON needs rewrite for this to work
                         solar_forecast["lat"] + "/" +
                         solar_forecast["long"] + "/" +
                         solar_forecast["declination"] + "/" +
                         solar_forecast["azimuth"] + "/" +
                         solar_forecast["kWpanels"] + "/"
                         )
# </editor-fold>

telegram = {
    "api_key":  "ZZZZZZZZ:XXXXXXXX", #api key from BotFather
    "chat_id": "-aaaaaaaaaa"          #chat id of group bot is in
}