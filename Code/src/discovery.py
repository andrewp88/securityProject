import requests
from bs4 import BeautifulSoup
import re


activePlugins=[]
vulnerablePlugins={"jtrt-responsive-tables":"SQL Injection, John","ad-manager-wd":"FileDownload","smartgooglecode":"XSS , Cookie Stealer","ultimate-product-catalogue":"SQL Injection"}


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
    activePlugins.append(scripts[0]['src'].split("/")[6])
    print("active plugins: " , activePlugins)


def urlPluginDiscovery(path,pUrl):
    url=pUrl+"/wp-content/plugins/"+path
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


def pluginListGeneration(pUrl):
    htmlPluginDiscovery(pUrl)
    urlPluginDiscovery("smart-google-code-inserter/",pUrl)
    urlPluginDiscovery("jtrt-responsive-tables/public/css/",pUrl)

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
    return vulnerablePluginCopy
