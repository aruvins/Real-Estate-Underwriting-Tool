import pandas as pd
import streamlit as st
from PIL import Image

def display_main_page():        
    st.title("Welcome to Financial Tools")
    st.write("Choose an option from the section above to navigate through different financial tools related to real estate.")

    st.header("Project Details")
    st.session_state.project_name = st.text_input(
        "Project Name", 
        value=st.session_state.get('project_name', 'Project Name')
    )

    st.session_state.company_name = st.text_input(
        "Company Name", 
        value=st.session_state.get('company_name', 'Your Company')
    )

    st.session_state.project_date = st.date_input(
        "Date", 
        value=st.session_state.get('project_date', pd.to_datetime("today").date())
    )

    st.subheader("Upload Project Images")
    uploaded_images = st.file_uploader("Choose image files", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if uploaded_images:
        for uploaded_image in uploaded_images:
            # Open the uploaded image
            image = Image.open(uploaded_image)
            
            # Resize the image to a smaller size if needed
            base_width = 400  # Set the desired width
            width_percent = (base_width / float(image.size[0]))
            height_size = int((float(image.size[1]) * float(width_percent)))
            image = image.resize((base_width, height_size), Image.LANCZOS)
            
            # Display the resized image
            st.image(image, caption=f"Uploaded Image: {uploaded_image.name}", use_column_width=False)
