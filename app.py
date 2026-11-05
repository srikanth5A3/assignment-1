import streamlit as st
st.set_page_config(
    page_title="Login Page",
    page_icon="🔐",
    layout="centered"
)


USERNAME = "srikanth"
PASSWORD = "chintu"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if not st.session_state.logged_in:

    st.title("🔐 Welcome Back!")
    st.subheader("Login to Your Account")

    username = st.text_input("Enter Username")

    password = st.text_input(
        "Enter Password",
        type="password"
    )

    if st.button("Login"):

        if username == USERNAME and password == PASSWORD:

            st.session_state.logged_in = True
            st.success("Login Successful!")
            st.rerun()

        else:
            st.error("Invalid Username or Password")

            
else:

    st.title("🎉 Welcome to Dashboard")
    st.success("You have successfully logged in!")

    st.write("Welcome chintu ")

    if st.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()