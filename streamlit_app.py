import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from streamlit_matplotlib import st_pyplot  # Import the streamlit_matplotlib library

def generate_animation():
    """Generates the animation using Matplotlib."""

    fig, ax = plt.subplots()
    ax.set_axis_off()

    # Initial image
    image = np.ones((100, 300), dtype=np.uint8) * 100
    im = ax.imshow(image, cmap='gray')

    def update(frame):
        image = np.ones((100, 300), dtype=np.uint8) * 100

        # Modify position and size based on frame
        cv2.circle(image, (75 + frame * 5, 50), 30, 30, -1)
        cv2.circle(image, (225 - frame * 5, 50), 30, 30, -1)
        rect_width = 20 + frame * 2
        cv2.rectangle(image, (140 - rect_width // 2, 20), (160 + rect_width // 2, 80), 200, -1)

        im.set_array(image)  # Update the image data
        ax.set_title(f"Frame {frame + 1}")
        return im,

    ani = animation.FuncAnimation(fig, update, frames=10, blit=True, repeat=False)
    return ani

if __name__ == "__main__":
    st.title("Animated Simulated X-ray Attenuation Image")
    ani = generate_animation()

    # Display the animation in Streamlit using st_pyplot
    st_pyplot(ani)