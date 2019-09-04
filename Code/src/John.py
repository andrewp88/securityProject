import SmartGoogleCodePlugin
import subprocess
import shlex

def attack():
    getPasswordFile()




def getPasswordFile():
    print("DEFAULT file to crack : resources/logindata.csv")
    file = input("Input file to crack , leave blank for default  : ")
    if(not file):
        file="C:\\Users\\andri\PycharmProjects\InfoSec\\venv\src\project\\resources\logindata.csv"
    wordList=input("Input word list file, leave blank for default : ")
    if(not wordList):
        wordList="C:\\Users\\andri\PycharmProjects\InfoSec\\venv\src\project\\resources\\rockyou.txt"
    johnPath=input("Insert the location of JohnTheRipper binary file : ")
    startJohn(file,wordList,johnPath)


def startJohn(passwords,wordlist,johnPath):
    call = 'john '+ passwords +' --wordlist='+wordlist

    johnProcess = subprocess.Popen(call, stdout=subprocess.PIPE, cwd=johnPath,shell=True)
    SmartGoogleCodePlugin.processList.append(johnProcess)

    poll = johnProcess.poll()
    if (poll == None):
        print("JOHN is running")
        johnProcess.wait()

    else:
        output, error = johnProcess.communicate()
        print(output + " |||| " + error)
        print("Process return code: " + string(phpProcess.returncode))

    print("John finished! \n")
    call2 = 'john ' + passwords + ' --show'

    johnProcess2 = subprocess.Popen(call, stdout=subprocess.PIPE, cwd=johnPath, shell=True)
    SmartGoogleCodePlugin.processList.append(johnProcess2)
    out, err = johnProcess2.communicate()

    poll = johnProcess2.poll()
    if (poll == None):
        print("JOHN 2 is running")
        johnProcess.wait()

    else:
        output, error = johnProcess2.communicate()
        print(output + " |||| " + error)
        print("Process return code: " + string(phpProcess.returncode))
    print(out)
    print("SECOND FINISH!")
#john passwords.csv --wordlist=rockyou.txt





