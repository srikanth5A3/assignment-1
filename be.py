from fastapi import FastAPI # importing one code from fastapi file
# import streamlit #importing entire file

obj=FastAPI()

@obj.post("/register")
def user_registration(abc:dict):# type annotation
    print(abc)
    # mysql
    return {
        "msg":"user data stored  successfully as new user "
    }



# command to strat be server :-- 
# uvicorn backend_filename:fasyapiobjvarname --reload
# uvicorn be:obj --reload 
# python -m uvicorn be:obj --reload 
# py -m uvicorn be:obj --reload 

int 
str
list 
dict
float
# pip install uvicorn
# @obj.get()
# @obj.post()
# @obj.put()
# @obj.delete()
