import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_and_display_image():
    """Generates and displays the simulated X-ray attenuation image."""

    # Create a grayscale image with a gray background
    image = np.ones((100, 300), dtype=np.uint8) * 100

    # Two circular, dark spots
    center1 = (75, 50)
    center2 = (225, 50)
    radius = 30
    image[
        (np.arange(100)[:, None] - center1[1]) ** 2 + (np.arange(300)[None, :] - center1[0]) ** 2 <= radius**2
    ] = 30

    image[
        (np.arange(100)[:, None] - center2[1]) ** 2 + (np.arange(300)[None, :] - center2[0]) ** 2 <= radius**2
    ] = 30

    # White rectangle in center of image
    rect_top_left = (140, 20)
    rect_bottom_right = (160, 80)
    image[rect_top_left[1]:rect_bottom_right[1], rect_top_left[0]:rect_bottom_right[0]] = 200

    # Display using Matplotlib
    st.pyplot(plt.imshow(image, cmap='gray'))
    plt.title("Simulated X-ray Attenuation")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    st.title("Simulated X-ray Attenuation Image")
    generate_and_display_image()