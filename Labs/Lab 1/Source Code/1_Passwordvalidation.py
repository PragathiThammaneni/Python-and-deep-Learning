# 1 .For any web application login, the user password need to be validated against database rules. For My UMKC web application following are the criteria for valid password:

import re  # imported the module that provides the regular expression regular expression
pw= input("Input your password : ")
temp = True
# Length should be in range 6-16 characters ,
# Should have at least one numeric ,Should have at least one special character,
# Should have at least one lowercase and at least one uppercase character.
while temp:
    if (len(pw)<6 or len(pw)>16):
        break
    elif not re.search("[0-9]",pw):
        break
    elif not re.search("[$@!*]",pw):
        break
    elif not re.search("[a-z]",pw):
        break
    elif not re.search("[A-Z]",pw):
        break
    else:
        print("Valid Password")
        temp=False
        break

if temp:
    print("Not a Valid Password")