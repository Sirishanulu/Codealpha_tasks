import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 AI Language Translation Tool")
st.write("Translate text between multiple languages instantly.")

text = st.text_area("Enter Text")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru"
}

source = st.selectbox("Source Language", list(languages.keys()))
target = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success(translated)