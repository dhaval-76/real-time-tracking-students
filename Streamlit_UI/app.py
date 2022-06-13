import streamlit as st
from multiapp import MultiApp
import SessionState
import student, teacher, home, signup
st.sidebar.title("🧭 Navigation Menu")


app=MultiApp()
app.add_app("Home", home.app)
app.add_app("Student", student.app)
app.add_app("Teacher", teacher.app)
# app.add_app("Sign Up", signup.app)

app.run()