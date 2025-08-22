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
    fig, ax = plt.subplots()
    ax.imshow(image, cmap='gray')
    ax.set_title("Simulated X-ray Attenuation")
    ax.axis('off')

    # Convert Matplotlib figure to NumPy array
    fig.canvas.draw()
    image_np = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image_np = image_np.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    #image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR) #we dont need cv2

    st.image(image_np, caption="Simulated X-ray Attenuation", use_container_width=True)
    plt.close(fig)  # Close the figure to prevent memory leaks

def main():
    st.title("Simulated X-ray Attenuation Image")
    st.write("""
This app generates a simple simulation of X-ray attenuation to demonstrate how different tissues appear on an X-ray image.
    """)
    generate_and_display_image()

if __name__ == "__main__":
    main()