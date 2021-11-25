# designed for forecast.solar api
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

twilio_config = {
    "account_sid":"ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "auth_token":"your_auth_token",
    "from":"+15017250604",  #text is sent from this number
    "to": [
    "+15558675309",         #recipient 1
    "+12223331234"          #recipient 2
    ]
}