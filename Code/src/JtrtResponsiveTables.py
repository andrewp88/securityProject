import RequestForger


def attack(url):

    print("SQL Injection attack.")
    username= input("Insert your username: ")
    password=input("Insert your password: ")
    result=RequestForger.login(url,username,password)
    while(not result):
        print("Your login failed. Username or password wrong. Insert them again!")
        username= input("Insert your username: ")
        password=input("Insert your password: ")
        result=RequestForger.login(url,username,password)

    RequestForger.test(url)