#!pip install gtts gradio (This needs installation to work alone.)

import gradio as gr
from gtts import gTTS

def text_to_speech(text, language):
    language_map = {
        "🇰🇷 Korean": "ko",
        "🇺🇸 English (AmE)": ("en", "us"),
        "🇬🇧 English (BrE)": ("en", "co.uk"),
        "🇫🇷 French": "fr",
        "🇪🇸 Spanish": ("es", "es"),
        "🇨🇳 Chinese": "zh-CN"
    }

    if isinstance(language_map[language], tuple):
        lang, tld = language_map[language]
        tts = gTTS(text=text, lang=lang, tld=tld)
    else:
        lang = language_map[language]
        tts = gTTS(text=text, lang=lang)

    tts.save("output.mp3")
    return "output.mp3"

# Define the Gradio interface
iface = gr.Interface(
    fn=text_to_speech,
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter text here..."),
        gr.Radio(["🇰🇷 Korean", "🇺🇸 English (AmE)", "🇬🇧 English (BrE)", "🇫🇷 French", "🇪🇸 Spanish", "🇨🇳 Chinese"], label="Language")
    ],
    outputs=gr.Audio(type="filepath"),
    title="Text to Speech Application (Multi-languages)",
    description="Enter text and choose a language to generate the corresponding audio."
)

# Launch the Gradio interface
iface.launch(debug=True)
