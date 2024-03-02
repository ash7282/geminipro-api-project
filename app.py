## invoice Extracter


from dotenv import load_dotenv

load_dotenv() ## load all environment from .env

import streamlit as st
import os
from PIL  import Image
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KE"))

## func to load gemini pro viion and get response

def get_gemini_response(input,image,prompt):
    ## loading the gemini model
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        #read the file into bytes
        bytes_data =uploaded_file.getvalue()
        image_parts = [
            {
                'mime_type': uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileExistsError("No file uploaded")
    
st.set_page_config(page_title="Image Extractor")

st.header("Gemini Application")
inpute=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an Image ...",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Upload Image",use_column_width=True)

submit=st.button("Tell me about the image")

input_prompt="""

"""

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,inpute)
    st.subheader("The Response is")
    st.write(response)
