import os
import sys


def clear_all():
    os.system("clear")



def boshmi(login_):
    return not bool(login_)



login = input("Loginni kiriting:").lower().strip()
password = input("Parolni kiriting:").lower().strip()
clear_all()

file = open("user.txt")
file.readline(6)
login_old = str(file.readline())
login_old = login_old[:-1]

file.close()
# print(login_old)

file = open("user.txt")
file.readline()
file.readline(9)
password_old = str(file.readline())
password_old = password_old[:-1]
file.close()
# print(password_old)
clear_all()

while login != login_old and password != password_old:
    clear_all()
    print("Parol yoki loginni xato kiritdingiz")
    login = input("Loginni kiriting:").lower().strip()
    password = input("Parolni kiriting:").lower().strip()


print("Siz tizimga kirdingiz.")
yangilash = input("Login yoki parolni o'zgartirasizmi? [y/n]: ").lower().strip()

tanlov = ['y', 'yes', 'no', 'n']
while yangilash not in tanlov:
    clear_all()
    print("Noto'g'ri belgi kiritdingiz. iltimos mos belgilardan birini tanlang!")
    yangilash = input("Login yoki parolni o'zgartirasizmi? [y/n]: ").lower().strip()
if yangilash in tanlov[2:]:
    sys.exit()
clear_all()
new_login = input("yangi loginni kiriting:").lower().strip()
new_password = input("yangi parolni kiriting:").lower().strip()

while boshmi(new_login) or boshmi(new_password):
    clear_all()
    print("Noto'g'ri belgi kiritdingiz. Iltimos qaytadan kiriting!")
    new_login = input("yangi loginni kiriting:").lower().strip()
    new_password = input("yangi parolni kiriting:").lower().strip()

file = open("user.txt", "w")
file.write(f"login={new_login}\n")
file.write(f"parol={new_password}")