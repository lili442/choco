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
confidence = st.slider("How confortable do you feel about structured products", min_value=0, max_value=100, step=1)
investing = st.selectbox("Do you invest or have a portfolio",
                             options=["Not at all", "I do a little", "I invest a lot"])
colors = st.multiselect('In what type of asset do you invest in',
                        options=['Bonds', 'Stocks', 'Commodities', 'FX', 'Crypto'])

col1, col2 = st.columns(2)
with col1:
    st.image("https://escpfinancesociety.files.wordpress.com/2020/10/financial-risk-management-improvements.jpg?w=1500", width=300)
    st.button("Like risk")
with col2:
    st.image("https://thumbs.dreamstime.com/z/risk-averse-concept-umbrella-to-shield-flat-kid-business-cartoon-design-risk-averse-concept-umbrella-to-shield-flat-kid-business-169576899.jpg", width=355)
    st.button("Hate risk")
