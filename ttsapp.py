import streamlit as st
from gtts import gTTS
import os

# Function to convert text to speech
def text_to_speech(text, language):
    language_map = {
        "🇰🇷 Korean": "ko",
        "🇺🇸 English (AmE)": ("en", "us"),
        "🇬🇧 English (BrE)": ("en", "co.uk"),
        "🇫🇷 French": "fr",
        "🇪🇸 Spanish": ("es", "es"),
        "🇨🇳 Chinese": "zh-CN"
    }

    # Select the appropriate language and top-level domain (if applicable)
    if isinstance(language_map[language], tuple):
        lang, tld = language_map[language]
        tts = gTTS(text=text, lang=lang, tld=tld)
    else:
        lang = language_map[language]
        tts = gTTS(text=text, lang=lang)

    # Save the audio file locally
    output_file = "output.mp3"
    tts.save(output_file)
    return output_file

# Streamlit app layout
st.title("Multi-Language Text to Speech")

# Input: text box for the user to input text
text_input = st.text_area("Enter the text you want to convert to speech:", "")

# Input: select the language
language = st.radio(
    "Choose the language for speech synthesis:",
    ("🇰🇷 Korean", "🇺🇸 English (AmE)", "🇬🇧 English (BrE)", "🇫🇷 French", "🇪🇸 Spanish", "🇨🇳 Chinese")
)

# Button to generate speech
if st.button("Generate Speech"):
    if text_input.strip() == "":
        st.error("Please enter some text to convert to speech.")
    else:
        # Generate the speech
        audio_file = text_to_speech(text_input, language)

        # Play the generated audio
        st.audio(audio_file)

        # Provide a download button for the generated audio
        with open(audio_file, "rb") as file:
            st.download_button(
                label="Download the speech as MP3",
                data=file,
                file_name="speech.mp3",
                mime="audio/mpeg"
            )

        # Clean up the saved audio file
        os.remove(audio_file)
