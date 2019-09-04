import requests
from bs4 import BeautifulSoup
import re
import discovery
import urlControls
import AdManagerWd
import SmartGoogleCodePlugin
import JtrtResponsiveTables
import ProductCatalogue





vulnerablePlugins={}
url = ""


class Main():
    def main(self):
        global url
        url = input("insert the url of the website to penetrate: ")
        while urlControls.main(url)==False:
            url = input("the inserted url is not correct, insert another url: ")

        choice=input("\n Insert the corresponding number for the desidered operation: \n 1. Plugin discovery \n 2. WpScan aggressive mode discovery \n Choice: ")
        while(not choice=='1' or choice=='2'):
            choice=input("Invalid choice! Choose between 1 and 2. New Choice: ")
        if(choice=='1'):

            vulnerablePlugins=discovery.main(choice,url)

            n=int(input("\n Chooce which plugin to attack or digit 0 to esc : "))
            while(not n==0):
                while(n>len(vulnerablePlugins)):
                    n=int(input("You have chosen an invalid option. Choose again: "))
                pluginName=list(vulnerablePlugins)[n-1]

                pluginChoice(pluginName)
                print("----------------------------------------------------------------------------")
                print("")
                discovery.listPrint()
                n=int(input("\n Attack completed! Choose another plugin to attack or digit 0 to esc: "))



        if(choice=='2'):

            print("wordpress discovery")

        if (SmartGoogleCodePlugin.processList):
            print("\n\nSome processes are running , do you want to close them?")
            yesno = input("Write Y to close otherwise the program will close and the processes will continue to run:")
            if (yesno == "Y"):
                for p in SmartGoogleCodePlugin.processList:
                    p.kill()
                print("\nAll processes had been closed")
            else:
                print("\nExit program, processes will continue to run")
                exit(0)
        else:
            print("\nExit program, no running processes")



def pluginChoice(choice):
    switcher={
        'ad-manager-wd': AdManagerWd.attack,
        'smartgooglecode': SmartGoogleCodePlugin.attack,
        'jtrt-responsive-tables': JtrtResponsiveTables.attack,
        'ultimate-product-catalogue': ProductCatalogue.attack
    }
    return switcher.get(choice, wrongPluginSelection)(url)

def wrongPluginSelection(url):
    choice=int(input("You have chosen an invalid option. Choose again: "))
    pluginName=list(vulnerablePlugins)[choice]
    pluginChoice(pluginName)



boostrapper=Main()
boostrapper.main()