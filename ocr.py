import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(['en'])

def extract_text(uploaded_file):

    image = Image.open(uploaded_file)

    image = np.array(image)

    result = reader.readtext(image)

    text = ""

    for item in result:
        text += item[1] + " "

    return text