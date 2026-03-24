import streamlit as st
import google.generativeai as genai

# 1. API Key Configuration
genai.configure(api_key="AIzaSyAcXc4GQ0FIV9a3wwLpqpnSU1Uq3a-JINw")

# 2. Page Settings
st.set_page_config(page_title="SmartChat Pro", page_icon="🚀", layout="centered")

# 3. Sidebar for info
with st.sidebar:
    st.title("About SmartChat")
    st.info("یہ آپ کا اپنا اے آئی اسسٹنٹ ہے جو گوگل کے Gemini ماڈل پر چلتا ہے۔")
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

st.title("🚀 SmartChat AI Pro")
st.caption("Powered by Google Gemini 1.5 Flash")

# 4. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Chat Input & Logic
if prompt := st.chat_input("کچھ پوچھیں..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Response
    with st.chat_message("assistant"):
        with st.spinner("سوچ رہا ہوں..."):
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)
                full_response = response.text
                st.markdown(full_response)
                # Save AI response
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"اوہ! کچھ مسئلہ ہوا ہے: {e}")
