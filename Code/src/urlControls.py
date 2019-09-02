import requests
from bs4 import BeautifulSoup
import re


def main(url):
    return urlControl(url)


def urlControl(url):
    if not url.startswith("http://"):
        return False
    response= requests.get(url)
    if(response.status_code==404):
        return False
    if(not response.text):
        return False
    if(not urlFooterControl(url)):
        return False
    if(not wpContentControl(url)):
        return False


    return True

def urlFooterControl(url):
    response=requests.get(url)
    #print(response.text);
    soup= BeautifulSoup(response.text,'html.parser')
    try :
        footer=soup.find('footer')

        div1=footer.find('div')
        div2=div1.find('div')
        a=div2.find('a')
        if "WordPress" in a.text:
            return True
    except:
        return False

def wpContentControl(url):
    response=requests.get(url)
    #print(response.text);
    soup= BeautifulSoup(response.text,'html.parser')
    scripts=soup.find_all('script', src=re.compile("^http://localhost/wp4.9/wordpress/wp-content/"))
    if scripts:
        return True

    return False