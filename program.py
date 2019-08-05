# Allows our program to open up firefox
from selenium import webdriver
# Allows us to plug in keys on the web driver
from selenium.webdriver.common.keys import Keys
#allows us to delay bot until webpage is loaded
import time



class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    def login (self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        # Searches place to put in login and password
        usernamelogin = bot.find_element_by_name("username")
        passwordlogin = bot.find_element_by_name("password")
        #Clears login in case username and password is already there
        usernamelogin.clear()
        passwordlogin.clear()
        #Puts in username and password then hits enter to login
        usernamelogin.send_keys(self.username)
        passwordlogin.send_keys(self.password)
        passwordlogin.send_keys(Keys.RETURN)
        time.sleep(5)
    def like_post(self,hashtag):
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(5)
        for i in range(1,3):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)

            posts = bot.find_elements_by_class_name('v1Nh3')
            links = [elem.find_element_by_css_selector('a').get_attribute('href') for elem in posts]
            for link in links:
                bot.get(link)
                try:
                    #Searches for the like button class
                    div=bot.find_elements_by_class_name('dCJp8')
                    #Searches within the button class for the grey heart to click on
                    lov = [el.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9').click() for el in div]
                    time.sleep(15)
                except Exception as ex:
                    #catches exceptions and does nothing for 30 seconds
                    time.sleep(30)
            

#Hides username and password from anyone that tries to clone this
#Create your own username and password text file to run this
username = open("username.txt","r")
password = open("password.txt","r")

ed = InstaBot(username.read(),password.read())
#Calls the login method to login into instagram
ed.login()
#Insert your own hashtag here
ed.like_post("meme")