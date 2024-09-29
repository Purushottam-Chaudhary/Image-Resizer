import streamlit as st
from PIL import Image
import io

# Function to resize the image
def resize_image(image, new_width, new_height):
    # Use Image.LANCZOS for better quality resizing
    resized_img = image.resize((new_width, new_height), Image.LANCZOS)
    return resized_img

# Streamlit app
def main():
    st.title("Image Resizer App")

    # Image uploader
    uploaded_image = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_image is not None:
        # Open the image
        image = Image.open(uploaded_image)
        st.image(image, caption='Original Image', use_column_width=True)

        # Get the original dimensions
        width, height = image.size
        st.write(f"Original Dimensions: {width} x {height}")

        # Input new dimensions
        new_width = st.number_input("Enter new width:", min_value=1, value=width)
        new_height = st.number_input("Enter new height:", min_value=1, value=height)

        # Resize the image when the button is clicked
        if st.button("Resize Image"):
            resized_image = resize_image(image, new_width, new_height)
            st.image(resized_image, caption='Resized Image', use_column_width=True)

            # Download option for resized image
            buffer = io.BytesIO()
            resized_image.save(buffer, format='PNG')
            buffer.seek(0)

            st.download_button(
                label="Download Resized Image",
                data=buffer,
                file_name="resized_image.png",
                mime="image/png"
            )

if __name__ == '__main__':
    main()
