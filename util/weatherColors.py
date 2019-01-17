# UncommonApp
# Dennis Chen, T Fabiha, Addison Huang, Michelle Tang
# P#02: The End
import json
from urllib.request import Request, urlopen
import urllib.parse
import random

def getLocation():
    '''
    Gets the location of the user using ipapi
    '''
    try:
        url = 'https://ipapi.co/json'
        response = urlopen(url)
        response = response.read()
        info = json.loads(response)
        city = info['city']
        state = info['region']
        country = info['country']
    except:
        city ='New York'
        state = "New York"
        country = "USA"
    return city,state,country
def getWeather():
    '''
    Gets the weather(not temperature) and time of day where the user lives using
    the airvisual API. Associates that weather and time of day with a keyword to
    be used later when generating colors
    '''
    location = list(getLocation())
    try:
        with open('keys/keys.json') as f:
            data = json.load(f)
    except:
        pass
    if location[2] == 'US':
        location[2] = 'USA'
    if location[0] == 'Brooklyn' or location[0] == 'Manhattan' or location[0] == 'Queens' or location[0] == 'Bronx' or location[0] == 'Staten Island':
        location[0] = 'New York'
    try:
        url = 'http://api.airvisual.com/v2/city?city=%s&state=%s&country=%s&key=%s' % (urllib.parse.quote(location[0]),urllib.parse.quote(location[1]),urllib.parse.quote(location[2]),data['weather'])
        response = urlopen(url)
        response = response.read()
        info = json.loads(response)
        weather = info['data']['current']['weather']['ic']
        keyword = ""
        if weather == '01d' or weather == '02d':
            keyword = "sun"
        elif weather == '01n' or weather == '02n':
            keyword = 'night'
        elif weather == '03d' or weather == '04d':
            keyword = 'cloud'
        else:
            keyword = "rain"
    except:
        keyword = random.choice(['sun','night','cloud','rain'])
    return keyword
def makePuzOnWeather():
    '''
    Based on keyword from getWeather(), gets colors that relate to that keyword
    using the colourlovers API
    '''
    url = "http://www.colourlovers.com/api/colors/?keywords=%s&format=json" % (getWeather())
    print(url)
    response = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(response).read()
    colors = json.loads(response)
    fourColors = [colors[0]['rgb'],colors[1]['rgb'],colors[2]['rgb'],colors[3]['rgb']]
    index = 0
    for each in fourColors:
        fourColors[index] = list(each.values())
        index += 1
    return fourColors
