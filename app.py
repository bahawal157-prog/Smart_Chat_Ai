import streamlit as st
import google.generativeai as genai

# یہاں اپنی Gemini API Key پیسٹ کریں
genai.configure(api_key="AIzaSyAcXc4GQ0FIV9a3WwLpqpnSU1Uq3a-JINw")
st.set_page_config(page_title="SmartChat AI", page_icon="🤖")
st.title("🤖 SmartChat AI"):
st.write("السلام علیکم! میں SmartChat AI ہوں۔ بتائیے، میں آج آپ کی کیا مدد کر سکتا ہوں؟")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("کچھ پوچھیں..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
