import re

regex = "^[a-z]\.[a-z]@fpmoz.sum.ba$"
regex2 = "^[a-z]([0-9]*)@sum.ba$"

while 1:
    email = input("Unesite e poštu:")
    eduid = input("EduId:")
    rezultat1 = re.search(regex, email)
    rezultat2 = re.search(regex2, eduid)
    if rezultat1 and rezultat2:
        print("Unos je ispravan")
        break
    else:
        print("Unos nije ispravan")