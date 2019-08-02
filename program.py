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


#Hides username and password from anyone that tries to clone this
username = open("username.txt","r")
password = open("password.txt","r")

ed = InstaBot(username.read(),password.read())
ed.login()
ed.like_post("meme")