import re

while 1:
    unos=input("Unesite neku riječ: ")
    regex="^K.*[0-5].*\s.*Ć$"
    result=re.findall(regex, unos)
    print(result)
    if result:
        print("Dobar unos!")
        break
    else:
        print("Pogrešan unos!")