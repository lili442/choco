import streamlit as st
st.title("Questions for students")
st.write("Here, you can answer to some questions in this form.")
st.write("We have to ask a few questions")
user_id = st.text_input("ID", value="Your ID", max_chars=7)
info = st.text_area("Share some information about you", "Put information here",
                    help='You can write about your hobbies or family')
age = st.number_input("Age", min_value=17, max_value=100, step=1)

finance = st.checkbox("Do you study finance?")
genre = st.radio("Which specialisation do you follow?",
                 options=['Investment Banking', 'Financial Markets', 'Corporate Finance'])
