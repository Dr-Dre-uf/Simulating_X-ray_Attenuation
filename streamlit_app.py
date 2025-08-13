import streamlit as st
import numpy as np
import cv2

def generate_xray_simulation():
    """Generates a simulated X-ray attenuation image."""

    image = np.ones((100, 300), dtype=np.uint8) * 100  # gray background

    # two circular, dark spots (representing low attenuation)
    cv2.circle(image, (75, 50), 30, 30, -1)
    cv2.circle(image, (225, 50), 30, 30, -1)

    # white rectangle in center of image (representing high attenuation)
    cv2.rectangle(image, (140, 20), (160, 80), 200, -1)

    return image

def main():
    st.title("Simulating X-ray Attenuation")

    # Generate the image
    image = generate_xray_simulation()

    # Display the image using Streamlit's st.image
    st.image(image, caption="Simulated X-ray Attenuation", use_column_width=True)

    # Explanation and questions
    st.subheader("Understanding X-ray Attenuation")
    st.write("""
X-rays pass through the body and are absorbed (or attenuated) by different tissues depending on their density and atomic number. The amount of attenuation determines how bright or dark a region appears on the X-ray image.

High attenuation materials (e.g., bone with high calcium content) absorb more X-rays and allow fewer to reach the detector. They appear brighter (white) on the X-ray image.

Low attenuation materials (e.g., air in lungs) allow most X-rays to pass through - they appear darker (black) on the X-ray image.

Intermediate tissues like muscle, fat, or organs absorb X-rays to a moderate degree. They appear in shades of gray.

**Biological Interpretation:**

*   Bones show up as bright white because they’re dense and highly attenuate X-rays.
*   Lungs are mostly air-filled, appearing dark, which helps radiologists detect infiltrates or fluid buildup.
*   Soft tissues such as liver, heart, or muscles appear in various gray levels based on their composition and density.
""")

    st.subheader("Think About It:")
    st.write("How does tissue contrast relate to X-ray attenuation? What kinds of materials appear brighter in an X-ray image? Darker? How might that relate to biology and anatomical structures?")

if __name__ == "__main__":
    main()