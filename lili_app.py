import streamlit as st
st.title("Form for the Users")
st.write("Here, you can answer to some questions in this form.")
st.write("We have to ask a few questions")
user_id = st.text_input("ID", value="Your ID", max_chars=7)
info = st.text_area("Share some information about you", "Put information here",
                    help='You can write about your hobbies or family')
