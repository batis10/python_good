user_name = "tom"
password = "123456789"


class AuthException(Exception):
    pass

def login(user: str, passw: str):
    if user_name == user and password == passw:
        print("login succesfull!!!")

    else:
        raise AuthException("please check your email or password")


i_username = input("plaase enter the username:\t")
i_password = input("plaase enter the password:\t")

try:
 login(i_username, i_password)
except AuthException as error:
   print(error)  






    