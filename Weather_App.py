########################### Welcome To Wheather App #################################

import requests
import json
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the speaking rate (you may need to adjust this value)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 60)  # You can experiment with different values here

    engine.runAndWait()

###################Input And URL################################################
print("Welcome TO Weather App Created by Abunnasar")
speak("Welcome TO Weather App Created by Abunnasar")

speak("Enter The name of the City: ")
c = input("Enter The name of the City: ")


url = f"http://api.weatherapi.com/v1/current.json?key=21fe31d86a7f431f83e60717232611&q={c}&aqi=no"


r = requests.get(url)
#r.raise_for_status() 
#print(r.text)
#print(type(r.text))
wdic = json.loads(r.text)
info1 = wdic["current"]["temp_c"]
info2 = wdic["current"]["temp_f"]
info3 = wdic["current"]["last_updated"]

#if url == :
#    print("You Must Be Connected With Internet")
#    speak("You Must Be Connected With Internet")

#################Speak StateMent#######################################

print(f"The Temperature of {c} city is celcius:{info1} and feranite:{info2}")
speak(f"The Temperature of {c} city is celcius:{info1}Degrees and feranite:{info2}Degrees")

if 12 < info1 > 23.5:
    print("It's Summer Weather")
    speak("It's Summer Weather")
elif 1.0 < info1 > 12.5:
    print("It's Winter Weather")
    speak("It's Winter Weather")
elif 24.0 < info1 > 36.5:
    print("I Think So it Will Rain")
    speak("I Think So it Will Rain")

print(f"Last Updated on {info3}")

print("You Can Ask Me More Citys Temperature!")
#print("If you want to quick type 'q'")    
speak(f"Last Updated on {info3}")
speak("You Can Ask Me More Citys Temperature!")
#speak("If you want to quick type 'q'")
