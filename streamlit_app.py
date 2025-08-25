import streamlit as st
import numpy as np

def generate_and_display_image():
    """Generates and displays the simulated X-ray attenuation image."""
    # Create a grayscale image with a gray background
    image = np.ones((100, 300), dtype=np.uint8) * 100

    # Two circular, dark spots
    center1 = (75, 50)
    radius1 = 30
    center2 = (225, 50)
    radius2 = 35  # Increased radius for the second circle
    inner_radius = 15 #Radius of inner light circle

    # Create a mask for the first circle
    y, x = np.ogrid[-center1[1]:100 - center1[1], -center1[0]:300 - center1[0]]
    mask1 = x*x + y*y <= radius1*radius1
    image[mask1] = 30

    # Create a mask for the second circle (outer dark circle)
    y, x = np.ogrid[-center2[1]:100 - center2[1], -center2[0]:300 - center2[0]]
    mask2 = x*x + y*y <= radius2*radius2
    image[mask2] = 30

    #Create a mask for the inner light circle
    y, x = np.ogrid[-center2[1]:100 - center2[1], -center2[0]:300 - center2[0]]
    mask_inner = x*x + y*y <= inner_radius*inner_radius
    image[mask_inner] = 100 #reset to background color

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