# Importing statements and API Initialization
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('english')


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
          Play an interactive story for you.\n
          Interracting with me is quite simple you just have to enter the number of the action you want me to do from the following list''')
    
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
        while main_menu_result == False:
            print("Please enter a valid input:")
            x = input(">>>")
            main_menu_result = main_menu_validate(x)
            
# Returning to Main Menu
def wiki_return_validate(x):
    """Validates input for wiki_return(). """
    if x in yes:
        mainmenu()
    elif x in no:
        wikichat()
    else:
        return False
    
    
def wiki_return():
    """Returns to the mainmenu() after wikichat()"""
    print("Would you like to return to the main menu?")
    x = input(">>>")
    if x == "exit":
        print("Ahsante! Kwaheri!")
        sys.exit()
    elif x == "return":
        mainmenu()
    else:
        wiki_validation_result = wiki_return_validate(x)
        if wiki_validation_result == False:
            while wiki_validation_result == False:
                print("Please enter a valid inpyt (yes or no):")
                x = input(">>>")
                wiki_validate_result = wiki_return_validate(x)


def wikichat():
    """This function will prompt the user to enter the name of article he/she wishes to interact with from the wikipedia"""
    print("What do you wish to learn about from the wikipedia?: ")
    x  =  input(">>>")
    if x == "exit":
        print("Ahsante! Goodbye!")
        sys.exit()
    elif x == "help":
        instructions()
    elif x == "return":
        mainmenu()
    else:
        wiki_validation_result = wiki_article_validate(x)
        if wiki_validation_result == False:
            while wiki_validation_result == False:
                print("Please enter a valid input: ")
                x = input(">>>")
                wiki_validation_result = wiki_article_validate(x)
        wiki_return()
        
        
# create a weather return function validation
def weather_return_validate(x):
    """Validates input for the weather function"""
    if x in yes:
        mainmenu()
    elif x in no:
        weatherchat()
    else:
        return False



#create a weather return function
def weather_return():
    """Takes you back to the mainmenu function"""
    print("Do you wish to return to the main menu?")
    x = input(">>>")
    if x == "exit":
        print("Ahsante sana! Kwaheri")
        sys.exit()
    elif x == "help":
        instructions()
    elif x == "return":
        mainmenu()
    else:
        weather_validation_result = weather_return_validate(x)
        if weather_validation_result == False:
            while weather_validation_result == False:
                print("Please enter a valid input (yes or no)")
                x = input(">>>")
                weather_validation_result = weather_return_validate(x)
                
                
# creating functions for the stories
def  story_return_validate(x):
    """
    This function will validate the input for the story return function
    """
    if x in yes:
        mainmenu()
    elif x in no:
        intro()
    else:
        return False
    
def story_return():
    """This function will prompt the user back to the main menu"""
    print("Do you wish to return to the main menu?")
    x  = input(">>>")
    if x == "exit":
        print("Ahsante sana!Goodbye!")
        sys.exit()
    elif x == "help":
        instructions()
    elif x == "return":
        mainmenu()
    else:
        story_validation_result = story_return_validate(x)
        if story_validation_result == False:
            while story_validation_result == False:
                print("Please enter a valid input")
                x = input(">>>")
                story_validation_result = story_return_validate(x)
                
#  created a function to receive summary of the wikipedia article 

def wiki_article_validate(articlename):
    """_summary_
    This function will validate the input of the wikichat()

    Args:
        articlename (_type_): _description_
    """
    page_py = wiki_wiki.page(articlename)
    if page_py.exists() == True:
       print(f"Here you go, {name}:\nPage - Title: {page_py.title}\nPage - Summary: {page_py._summary}")
 
    else:
        return False
    return page_py

# functions for local weather report
def localweather(place):
    """This function will validate if the location inputed is real or just some random location

    Args:
        place  will server as an input x value 
    """
    mgr = owm.weather_manager()
    try:
        observation = mgr.weather_at_place(place)
    except:
        return False
    w = observation.weather
    print("Temperature: {}°C\nMax Temperature: {}°C\nMin Temperature: {}°C\nFeels Like: {}°C\nHumidity: {}%\nWind Speed: {}M/s\nWind Direction: {}°".format(
    w.temperature('celsius')["temp"],
    w.temperature('celsius')["temp_max"],
    w.temperature('celsius')["temp_min"],
    w.temperature('celsius')["feels_like"],
    w.humidity,
    w.wind()["speed"],
    w.wind()["deg"]
    ))
    
def weather():
    """
    with this function the user will be prompted to enter the name of the city afterwards another function will have to run to validate it
    
    """
    x = input("Enter the city that you want the weather of:\n >>> ")
    local_weather_validation = localweather(x)
    if local_weather_validation == False:
        while local_weather_validation == False:
            x = input("Please enter an exact city name:")
            local_weather_validation = localweather(x)


def weather_chat_validate(x):
    """
    After an input has been given to the waetherchat function this will validate it

    Args:
        x (choice): The selection of the user of what wants to be done in the weatherchat()
    """
    if x == "1":
        ip = urllib.request.urlopen('https://ip.42.pl/raw').read().decode('utf8')
        location = geo_lookup.get_location(ip)
        weatherlocation = location["city"]
        print(f"Here is your weather for{weatherlocation}(Powered by OpenWeathermap)")
        localweather(weatherlocation)
    elif x == "2":
        if __name__ == '__main__':
            weather()
    else:
        return False
    
# main function for the weather

def weatherchat():
    """This function will have the user choose whether to input location manually or automatically
    """
    
    x = input("Do you want me to retrieve your location, or do you want to manually enter your location? (Powered by OpenWeatherMap)\n[1] Automatically Retrieve Location*\n[2] Manually Enter Location\n*If you use a cloud-based interpreter, I will not be able to find the proper IP address of your computer, and thus I will not return the proper weather for your location.\nPlease run this action on a local machine for full functionality.\nAlso, be sure to turn off your VPN or Internet Proxy if you have one on for accurate results.\n>>> ")
    if x == "exit":
        print("Ahsante! Kwaheri!")
        sys.exit()
    elif x == "help":
        instructions()
    elif x == "return":
        mainmenu()
    else:
        weather_chat_validate = weather_chat_validate(x)
        if weather_chat_validation == False:
            while weather_chat_validation == False:
                x = input("Please enter a valid input:\n >>> ")
                weather_chat_validation = weather_chat_validate(x)
        weather_return()