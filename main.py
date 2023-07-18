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

# Useful functions to be used in the program
 # A function to return the user name
def returnname():
    print("What is your name buddy?(Enter only a single name)")
    global name
    name = input(">>>")
    if name == "exit":
        print("Ahsante Sana!Karibu Tena")
        sys.exit()
    elif name == "help":
        instructions()
    elif name == "return":
        mainmenu()
    else:
        print("Wow Such a cool name", name, "!")
        
def instructions():
    print('''I am your virtual assistant with wide feature set:\n
          I can find information about something you want to learn\n
          Retrieve current local weather\n
          Play an interactive story for you.''')
    print("Interracting with me is queit simple you just have to enter the number of the action you want me to do from the following list")