
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import src.helper as helper



load_dotenv()

# set API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# implement streamlit app
st.set_page_config(page_title="Textual Image Info Extractor")

st.header("Ask me about your Textual Image...")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose your image.", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

submit = st.button("Tell me about the image.")

input_prompt = """
You are an expert in understanding textual images. You will receive
an input image and given that I would like to ask you to answer the
questions.
"""

if submit:
    image_info =  helper.input_image_info(uploaded_file)
    response = helper.get_gemini_response(input, image_info, input_prompt)

    st.subheader("The response is")
    st.write(response)