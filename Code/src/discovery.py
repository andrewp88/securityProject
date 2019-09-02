import requests
from bs4 import BeautifulSoup
import re


activePlugins=[]
vulnerablePlugins={"jtrt-responsive-tables":"SQL Injection, John","ad-manager-wd":"FileDownload","smartgooglecode":"SQL Injection"}

def main(choice):
    if(choice=='1'):
        pluginListGeneration()
        return vulnerablePlugins
    else:
        print("WpScan")

def htmlPluginDiscovery():
    response=requests.get("http://localhost/wp4.9/wordpress")
    #print(response.text);
    soup= BeautifulSoup(response.text,'html.parser')
    scripts=soup.find_all('script', src=re.compile("^http://localhost/wp4.9/wordpress/wp-content/plugins/"))
    #print("scripts: ",scripts);
    activePlugins.append(scripts[0]['src'].split("/")[7])


def urlPluginDiscovery(path):
    url="http://localhost/wp4.9/wordpress/wp-content/plugins/"+path
    response=requests.get(url)
    if(path=="smart-google-code-inserter/"):
        smartGoogleDiscover(response.text)
    elif (path=="jtrt-responsive-tables/public/css/"):
        jtrtTablesDiscover(response)



def jtrtTablesDiscover(response):
    if not response.status_code==404:
        activePlugins.append("jtrt-responsive-tables")


def smartGoogleDiscover(response):
    soup= BeautifulSoup(response,'html.parser')
    href=soup.find_all('a',href=re.compile("\.ph"
                                           "p$"))
    if href:
        activePlugins.append(href[0].text.split(".")[0])

    else:
        print("this plugin is not active")


def pluginListGeneration():
    htmlPluginDiscovery()
    urlPluginDiscovery("smart-google-code-inserter/")
    urlPluginDiscovery("jtrt-responsive-tables/public/css/")

    activePluginCopy=activePlugins.copy()
    vulnerablePluginCopy=vulnerablePlugins.copy()

    for x in vulnerablePlugins.keys():
        if x not in activePlugins:
            del vulnerablePluginCopy[x]

    for y in activePlugins:
        if y in activePluginCopy:
            activePluginCopy.remove(y)

    if len(activePluginCopy)!=0:
        print("\n Active Plugins: ")
        for z in activePluginCopy:
            print(z)

    if len(vulnerablePluginCopy)!=0:
        print("\n Vulnerable Plugins: ")
        counter=1;
        for x, y in vulnerablePluginCopy.items():
            string=str(counter)+ ": "+x +" --> Possible attacks: " + y
            print(string)
            counter+=1

