import streamlit as st
import google.generativeai as genai

# 1. API Key Configuration
genai.configure(api_key="AIzaSyAcXc4GQ0FIV9a3wwLpqpnSU1Uq3a-JINw")

# 2. Page Settings (Icon with Robot & Urdu text)
st.set_page_config(page_title="SmartChat AI", page_icon="🤖", layout="centered")

# --- لوگو اور ٹائٹل کا سیکشن ---
# ہم CSS استعمال کر کے ایک کسٹم لوگو ڈیزائن بنائیں گے

st.markdown("""
<style>
    .logo-container {
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #f0f2f6;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 25px;
        border: 2px solid #007bff;
    }
    .logo-icon {
        font-size: 50px;
        margin-right: 20px;
        color: #007bff;
    }
    .logo-text-container {
        display: flex;
        flex-direction: column;
    }
    .logo-main-text {
        font-size: 32px;
        font-weight: bold;
        color: #31333F;
        margin: 0;
    }
    .logo-sub-text {
        font-size: 16px;
        color: #555;
        margin: 0;
        font-style: italic;
    }
    .urdu-text {
        font-family: 'Noto Nastaliq Urdu', serif;
        font-size: 24px;
        color: #007bff;
        margin-top: 5px;
    }
</style>

<div class="logo-container">
    <div class="logo-icon">🤖</div>
    <div class="logo-text-container">
        <div class="logo-main-text">SmartChat AI</div>
        <div class="logo-sub-text">Your Urdu AI Assistant</div>
        <div class="urdu-text">سمارٹ چیٹ اے آئی</div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------

# 3. Sidebar for info
with st.sidebar:
    st.title("SmartChat Settings")
    st.info("یہ آپ کا اپنا اے آئی اسسٹنٹ ہے۔")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# 4. Initialize & Display Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Chat Logic
if prompt := st.chat_input("کچھ پوچھیں..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("جواب تیار کر رہا ہوں..."):
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"ایرر: {e}")
