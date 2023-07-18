# Importing statements and API Initialization
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')


#Initializing OpenWeatherMap API
from pyowm import OWM
owm = OWM('YOUR_OWM_API_KEY')

# Initializing ipstack Geolocation API
import urllib.request
from ipstack import GeoLookup
geo_lookup = GeoLookup("YOUR_IPSTACK_API_KEY")

#regular modules used
import sys
import time


# User responses 
answer_A = ["A", "a", "A.", "a."]
answer_B = ["B", "b", "B.", "b."]
answer_C = ["C", "c", "C.", "c."]
yes = ["Y", "y", "Yes", "yes", "YES"]
no = ["N", "n", "No", "no", "NO"]

