import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt

def generate_static_image():
    """Generates a static simulated X-ray attenuation image."""

    image = np.ones((100, 300), dtype=np.uint8) * 100  # gray background

    # two circular, dark spots
    cv2.circle(image, (75, 50), 30, 30, -1)
    cv2.circle(image, (225, 50), 30, 30, -1)

    # white rectangle in center of image
    cv2.rectangle(image, (140, 20), (160, 80), 200, -1)

    # Display using Matplotlib
    fig, ax = plt.subplots()
    ax.imshow(image, cmap='gray')
    ax.set_title("Simulated X-ray Attenuation")
    ax.axis('off')
    return fig

if __name__ == "__main__":
    st.title("Simulated X-ray Attenuation Image")
    fig = generate_static_image()
    st.pyplot(fig)