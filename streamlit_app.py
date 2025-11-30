import streamlit as st
import numpy as np

# =====================================================================
# SCRIPT 1 — Simulated X-ray Attenuation Image
# =====================================================================

def app_xray_simulation():
    st.title("Simulated X-ray Attenuation Image")
    st.write("""
    This app generates a simple simulation of X-ray attenuation to demonstrate how 
    different tissues appear on an X-ray image.
    """)
    generate_and_display_image()


def generate_and_display_image():
    """Generates and displays the simulated X-ray attenuation image."""
    
    # Create a grayscale image with a gray background
    image = np.ones((100, 300), dtype=np.uint8) * 100

    # Two circular, dark spots
    center1 = (75, 50)
    radius1 = 30
    center2 = (225, 50)
    radius2 = 35
    inner_radius = 15

    # First dark circle
    y, x = np.ogrid[-center1[1]:100 - center1[1], -center1[0]:300 - center1[0]]
    mask1 = x*x + y*y <= radius1 * radius1
    image[mask1] = 30

    # Second dark circle
    y, x = np.ogrid[-center2[1]:100 - center2[1], -center2[0]:300 - center2[0]]
    mask2 = x*x + y*y <= radius2 * radius2
    image[mask2] = 30

    # Inner bright circle inside circle 2
    mask_inner = x*x + y*y <= inner_radius * inner_radius
    image[mask_inner] = 100

    # White rectangle
    rect_top_left = (140, 20)
    rect_bottom_right = (160, 80)
    image[rect_top_left[1]:rect_bottom_right[1], rect_top_left[0]:rect_bottom_right[0]] = 200

    # Display image
    st.image(image, caption="Simulated X-ray Attenuation", channels="GRAY", use_container_width=True)




# =====================================================================
# SCRIPT 2 — Pixel Intensity Histogram App
# =====================================================================

def app_intensity_histogram():
    st.title("Pixel Intensity Histogram App")

    # Create a synthetic image
    width, height = 200, 200
    image = create_synthetic_image(width, height)

    # Calculate histogram
    histogram_data = calculate_histogram(image)

    # Prepare vertical peak lines (for visualization)
    air_line = [0] * 30 + [9000] * 5 + [0] * (256 - 35)
    soft_tissue_line = [0] * 100 + [1000] * 5 + [0] * (256 - 105)
    bone_line = [0] * 200 + [21000] * 5 + [0] * (256 - 205)

    # Display the histogram with indicators
    st.write("### Synthetic Pixel Intensity Peaks")
    st.line_chart({
        "Air": air_line,
        "Soft Tissue": soft_tissue_line,
        "Bone": bone_line,
    })


def create_synthetic_image(width, height):
    """Creates a synthetic image with three intensity levels."""
    image = np.zeros((height, width), dtype=np.uint8)

    # Simulate air (30)
    image[image < 50] = 30
    # Soft tissue (100)
    image[(image >= 50) & (image < 150)] = 100
    # Bone (200)
    image[image >= 150] = 200

    return image


def calculate_histogram(image):
    """Calculates histogram using NumPy."""
    pixels = image.flatten()
    hist, bins = np.histogram(pixels, bins=256, range=[0, 256])
    return hist



# =====================================================================
# MAIN APP WITH SIDEBAR
# =====================================================================

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio(
        "Choose an app:",
        ["Simulated X-ray Image", "Pixel Intensity Histogram"]
    )

    if selection == "Simulated X-ray Image":
        app_xray_simulation()
    elif selection == "Pixel Intensity Histogram":
        app_intensity_histogram()


if __name__ == "__main__":
    main()
