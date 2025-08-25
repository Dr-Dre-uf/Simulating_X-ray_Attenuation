import streamlit as st
import numpy as np

def generate_and_display_image():
    """Generates and displays the simulated X-ray attenuation image."""
    # Create a grayscale image with a gray background
    image = np.ones((100, 300), dtype=np.uint8) * 100
    # Two circular, dark spots
    center1 = (75, 50)
    center2 = (225, 50)
    radius = 30

    for y in range(100):
        for x in range(300):
            dist1 = np.sqrt((y - center1[1])**2 + (x - center1[0])**2)
            dist2 = np.sqrt((y - center2[1])**2 + (x - center2[0])**2)

            if dist1 <= radius:
                image[y, x] = 30
            if dist2 <= radius:
                image[y, x] = 30

    # White rectangle in center of image
    rect_top_left = (140, 20)
    rect_bottom_right = (160, 80)
    image[rect_top_left[1]:rect_bottom_right[1], rect_top_left[0]:rect_bottom_right[0]] = 200

    # Display the image in Streamlit
    st.image(image, caption="Simulated X-ray Attenuation", channels="GRAY", use_container_width=True)

def main():
    st.title("Simulated X-ray Attenuation Image")
    st.write("""
This app generates a simple simulation of X-ray attenuation to demonstrate how different tissues appear on an X-ray image.
    """)
    generate_and_display_image()

if __name__ == "__main__":
    main()