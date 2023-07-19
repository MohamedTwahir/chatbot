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
    
def main_menu_validate(x):
    if x == "1":
        wikichat()
    elif x == "2":
        weatherchat()
    elif x == "3":
        intro()
    elif x == "exit":
        print("Ahsante! Kwaheri")
        sys.exit()
    elif x == "help":
        instructions()
        time.sleep(1)
        mainmenu()
    elif x == "return":
        mainmenu()
    else:
        return False
    

def mainmenu():
    print("\n What can i assist you with? Type the choice that corresponds to the action")
    time.sleep(1)
    print('''[1] Find a topic on wikipedia that you want to learn about\n
          [2] Retrieve the current Weather Condition in your location\n
          [3] Play an Interactive story mode\n''')
    x = input(">>>")
    main_menu_result == main_menu_validate(x)
    if main_menu_result == False:
        print("Please enter a valid input:")
        x = input(">>>")
        main_menu_result = main_menu_validate(x)