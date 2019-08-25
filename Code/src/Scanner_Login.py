#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import re

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))



def htmlPluginDiscovery():
    response=requests.get("http://192.168.1.55/wp4.9/wordpress");
    #print(response.text);
    soup= BeautifulSoup(response.text,'html.parser');
    scripts=soup.find_all('script', src=re.compile("^http://localhost/wp4.9/wordpress/wp-content/plugins/") )
    #print("scripts: ",scripts);
    plugin= scripts[0]['src'].split("/")[7];
    print(plugin);


def urlPluginDiscovery():
    response=requests.get("http://192.168.1.55/wp4.9/wordpress/wp-content/plugins/smart-google-code-inserter/");
    soup= BeautifulSoup(response.text,'html.parser');
    href=soup.find_all('a',href=re.compile("\.php$"));
    if href:
        plugin=href[0].text;
        print(plugin);
    else:
        print("this plugin is not active");



def login(url,username,password):
    wp_login = url+'/wp-login.php'
    wp_admin = url+'/wp-admin/'
    

    with requests.Session() as s:
        headers1 = { 'Cookie':'wordpress_test_cookie=WP Cookie check' }
        datas={
            'log':username, 'pwd':password, 'wp-submit':'Log In',
            'redirect_to':wp_admin, 'testcookie':'1'
        }
        s.post(wp_login, headers=headers1, data=datas)
        resp = s.get(wp_admin)
        print(resp.text)


login('http://192.168.1.55/wp4.9/wordpress','admin2','admin')
