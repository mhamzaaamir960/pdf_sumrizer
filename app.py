import streamlit as st
from PIL import Image
import PyPDF2


st.set_page_config(
    page_title="PDF Summarizer",
    page_icon=":robot:"
)

# st.text_input("Upload pdf")


# name = st.text_input("Enter your nmae: ")
# st.write(f'Name: {name}')


# if st.button("click me"):
#     st.write("clicked me")


# st.dataframe({"Name": ["Hamza","Omer","ALi"], "Age": [20,25,35]})

# upload_image = st.file_uploader("Upload file", type="pdf")

# if upload_image is not None:
#     image = Image.open(upload_image)

#     st.image(image, caption="Upload Image", use_column_width=True)
# else: 
#     st.write("Please upload an image file!")

st.title("Streamlit App interface Design")


st.sidebar.title("Navigation")
st.sidebar.write("This is sidebar")
option  = st.sidebar.selectbox("Choose a feature",("Upload Image","Upload pdf"))

#  Main content

st.write("Welcome to streamlit app interface design")
if option == "Upload Image":
    st.write("Upload an Image")
    upload_image = st.file_uploader("Choose an image file", type=["jpg","png","jpeg"])
    if upload_image is not None:
        image = Image.open(upload_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    else:
        st.write("Please upload a file")

elif option == "Upload pdf":
    st.write("Upload a pdf file")
    upload_pdf = st.file_uploader("Choose a pdf file", type=["pdf"])
    if upload_pdf is not None:
        reader = PyPDF2.PdfReader(upload_pdf)
        pdf_text = ""
        for page_num in range(len(reader.pages)):
            pdf_text += reader.pages[page_num].extract_text()
        st.write("Extracted text from pdf")
        st.write(pdf_text)
    else:
        st.write("Please upload a PDF file")
 