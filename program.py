# Allows our program to open up firefox
from selenium import webdriver
# Allows us to plug in keys on the web driver
from selenium.webdriver.common.keys import Keys
# Allows us to check if the webpage has loaded
from selenium.webdriver.support import expected_conditions 

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    def login (self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        bot.implicitly_wait(5)

username = open("username.txt","r")
password = open("password.txt","r")

ed = InstaBot(username,password)
ed.login()