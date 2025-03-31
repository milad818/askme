

import google.generativeai as genai



def get_gemini_response(input, image, prompt):
    
    # load model
    model = genai.GenerativeModel('gemini-1.5-flash') # it may raise an error if the model is deprecated
    # generate response
    response = model.generate_content([input, image[0], prompt])
    # return response
    return response.text



def input_image_info(uploaded_file):

    if uploaded_file is not None:
        image_bytes = uploaded_file.getvalue()

        image_info = [
            {
                "mime_type": uploaded_file.type,
                "data": image_bytes
            }
        ]
        
        return image_info
    else:
        raise FileNotFoundError("No file Uploaded!")