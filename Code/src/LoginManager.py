
import requests
from bs4 import BeautifulSoup

session=None

def login(url,username,password):
    wp_login = url+'/wp-login.php'
    wp_admin = url+'/wp-admin/'


    with requests.Session() as s:
        global session
        session=s
        headers1 = { 'Cookie':'wordpress_test_cookie=WP Cookie check' }
        datas={
            'log':username, 'pwd':password, 'wp-submit':'Log In',
            'redirect_to':wp_admin, 'testcookie':'1'
        }
        resp=s.post(wp_login, headers=headers1, data=datas)
    return loginControl(resp.text)

        #controllo se il login è stato effettuato
        #estrarre la sessione
        #con la sessione fare la nuova richiesta


def loginControl(response):
    soup=BeautifulSoup(response,'html.parser')
    div= soup.find_all('div', {"id":"login"})
    if(div):
        finalDiv=div[0].find_all('div', {"id": "login_error"})

        if(finalDiv):
            print("Login Unsuccesful!")
            return False

    print("Succesfully Logged In!")
    return True
