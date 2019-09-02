import requests
from bs4 import BeautifulSoup
import re
import discovery
import urlControls
import AdManagerWd
import SmartGoogleCodePlugin
import JtrtResponsiveTables





vulnerablePlugins={}
vulnerabilities=['1. XSS attack','2. File Download','3. SQL Injection','4. Reverse shell']


class Main():
    def main(self):
        url = input("insert the url of the website to penetrate: ")
        while urlControls.main(url)==False:
            url = input("the inserted url is not correct, insert another url: ")


        choice=input("\n Insert the corresponding number for the desidered operation: \n 1. Plugin discovery \n 2. WpScan aggressive mode discovery \n Choice: ")
        while(not choice=='1' or choice=='2'):
            choice=input("Invalid choice! Choose between 1 and 2. New Choice: ")
        if(choice=='1'):

            vulnerablePlugins=discovery.main(choice)
            n=int(input("\n Chooce which plugin to attack: "))

            while(n>len(vulnerablePlugins)):
                n=int(input("You have chosen an invalid option. Choose again: "))
            pluginName=list(vulnerablePlugins)[n-1]
            pluginChoice(pluginName)

        if(choice=='2'):
            print("wordpress discovery")




def pluginChoice(choice):
    switcher={
        'ad-manager-wd': AdManagerWd.attack,
        'smartgooglecode': SmartGoogleCodePlugin.attack,
        'jtrt-responsive-tables': JtrtResponsiveTables.attack
    }
    return switcher.get(choice, wrongPluginSelection)()

def wrongPluginSelection():
    choice=int(input("You have chosen an invalid option. Choose again: "))
    pluginName=list(vulnerablePlugins)[choice]
    pluginChoice(pluginName)


def XSSAttack():
    print("XSS attack chosen")

def SQLAttack():
    print("SQL Injection attack chosen")

def fileDownloadAttack():
    print("File Download attack chosen")

def reverseShellAttack():
    print("XSS attack chosen")


def attacksList():
    print("\n Possible attacks:")
    for x in vulnerabilities:
        print(x)



options= {'1': XSSAttack, '2':fileDownloadAttack, '3':SQLAttack ,'4':reverseShellAttack}


m=Main()
m.main()