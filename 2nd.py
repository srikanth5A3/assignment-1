from asyncio import log


def dashboard(loggedin_email):
    print("welcome dashboard")
    print("welcome", loggedin_email)

r_email = "guvvasrikanth45@gmail.com"
r_password = "12345678"

def login():
    l_email = input("enter email to login: ")
    l_password = input("enter password to login: ")
    if r_email == l_email and r_password == l_password:
        return {"status": True, "msg": "login successfull", "email": l_email}
    else:
        return {"status": False, "msg": "invalid credentials"}

login_obj = login()

if login_obj["status"] == True:
    dashboard(login_obj["email"])
else:
    print(login_obj["msg"])
 