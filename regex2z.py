import re

unos_email = input("Unesite e-mail: ")
regex_email = "(^[a-zA-Z].*)[.]([a-zA-Z].*)@fpmoz.sum.ba$"
rezultat_email = re.match(regex_email, unos_email)

unos_eduid = input("Unesite eduId: ")
regex_eduid = "^([a-zA-Z])([a-zA-Z].*)[0-9]*@sum.ba$"
rezultat_eduid = re.match(regex_eduid, unos_eduid)

if rezultat_email:
    print("Email je ispravan.")
else:
    print("Email nije ispravan.")

if rezultat_eduid:
    print("EduId je ispravan.")
else:
    print("EduId nije ispravan.")
