import streamlit as st

# Title of App
st.title("Atlanta Ledger")

# Assignment Data
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Team 73, Web Development - Section D")
st.subheader("Emma Norman, Jaeyun Park")

# TODO (optional): Add a group photo to the images folder and show it here, for example:
st.image("images/emma.JPG")
st.image("images/JP.jpg")

# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description

st.write("""
Welcome to our Streamlit Web Development app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. Atlanta Spending Explorer: See charts of spending seperated by category and top vendors
2. Budget Chat Bot: Answers questions about city budgets and how municipal spending works
3. Spending Chat Bot: AI agent that looks up checkbook data and answers questions
""")
