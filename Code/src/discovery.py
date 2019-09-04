import requests
from bs4 import BeautifulSoup
import re


activePlugins=[]
vulnerablePlugins={"jtrt-responsive-tables":"SQL Injection, John","ad-manager-wd":"FileDownload","smartgooglecode":"XSS , Cookie Stealer","ultimate-product-catalogue":"SQL Injection","loginizer":"Stored XSS attack"}
vulnerablePluginCopy={}

def main(choice,pUrl):
    if(choice=='1'):
        return pluginListGeneration(pUrl)
    else:
        print("WpScan")

def htmlPluginDiscovery(pUrl):
    response=requests.get(pUrl)
    #print(response.text);
    soup= BeautifulSoup(response.text,'html.parser')
    pluginString = "^"+pUrl + "/wp-content/plugins/"
    scripts=soup.find_all('script', src=re.compile(pluginString))
    #print("scripts: ",scripts);

    stringSplitted=scripts[0]['src'].split("/")
    i=stringSplitted.index("plugins")
    activePlugins.append(stringSplitted[i+1])


def urlPluginDiscovery(path,pUrl):
    url=pUrl+"/wp-content/plugins/"+path
    response=requests.get(url)
    if(path=="smart-google-code-inserter/"):
        smartGoogleDiscover(response.text)
    elif (path=="jtrt-responsive-tables/public/css/"):
        jtrtTablesDiscover(response)
    elif (path == "metronet-tag-manager/tinyMCE/"):
        metronetTagmanager(response)
    elif (path == "loginizer/ipv6/"):
        loginizer(response)


def loginizer(response):
    if not response.status_code == 404:
        activePlugins.append("loginizer")

def metronetTagmanager(response):
    if not response.status_code == 404:
        activePlugins.append("metronet-tag-manager")



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


def pluginListGeneration(pUrl):
    htmlPluginDiscovery(pUrl)
    urlPluginDiscovery("smart-google-code-inserter/",pUrl)
    urlPluginDiscovery("jtrt-responsive-tables/public/css/",pUrl)
    urlPluginDiscovery("metronet-tag-manager/tinyMCE/",pUrl)
    urlPluginDiscovery("loginizer/ipv6/",pUrl)
    global vulnerablePluginCopy
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

    listPrint()

    return vulnerablePluginCopy

def listPrint():
    if len(vulnerablePluginCopy)!=0:
        print("\n Vulnerable Plugins: ")
        counter=1;
        for x, y in vulnerablePluginCopy.items():
            string=str(counter)+ ": "+x +" --> Possible attacks: " + y
            print(string)
            counter+=1