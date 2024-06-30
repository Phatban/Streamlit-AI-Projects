"""
main.py

This is the main module for the Object Detection application using Streamlit.
It provides the user interface and integrates the object detection functionality.

Functions:
    main(): Run the Streamlit application.

This module depends on the object_detection module for image processing functionality.
"""

import streamlit as st
from PIL import Image
import numpy as np
from object_detection import process_image, annotate_image


def main():
    """
    Main function to run the Streamlit app for object detection.
    """
    st.title('Object Detection for Images')

    uploaded_file = st.file_uploader(
        "Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button('Detect Objects'):
            image_np = np.array(image)
            detections = process_image(image_np)
            annotated_image = annotate_image(image_np, detections)
            st.image(annotated_image, caption='Detected Objects',
                     use_column_width=True)


if __name__ == "__main__":
    main()
