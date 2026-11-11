import streamlit as st
import requests as req
st.title("Day1 Streamlit Class")

t1,t2=st.tabs(["Login","Register"])

# st.write(t1)
# st.write(t2)

with t1:
    with st.form("LoginForm"):
        st.subheader("LoginForm")
        email=st.text_input("Email",placeholder="Enter email here to login")
        password=st.text_input("Password",type="password",placeholder="Enter password to login")
        role=st.selectbox("Choose yr role below ",["","Trainer","Student"])
        login_btn=st.form_submit_button("Login") # True

        if login_btn:
            st.write({"email":email,"password":password,"role":role})
with t2:
    with st.form("RegisterForm"):
        st.subheader("RegisterForm")
        name=st.text_input("Name",placeholder="Enter yr name")
        email=st.text_input("Email",placeholder="Enter yr email here")
        password=st.text_input("Password",placeholder="Enter password here",type="password")            
        Confirm_Password=st.text_input("Confirm_Password",placeholder="Enter password again",type="password")  
        role=st.selectbox("Choose Role ",["","Trainer","Student"])
        regsiter_btn=st.form_submit_button("Register")

        if regsiter_btn:
            if password == Confirm_Password:

                payload={
                    "name":name,
                    "email":email,
                    "password":password,
                    "confirm-password":Confirm_Password,
                    "role":role
                }

                res=req.post("http://127.0.0.1:8000/register",json=payload)
                # st.write(res)
                if res.status_code == 200:
                    st.write(res.json())

            else:
                st.error("passwords doesnt match")    

