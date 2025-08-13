import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_animation():
    """Generates the animated simulated X-ray attenuation image."""

    fig, ax = plt.subplots()
    ax.set_axis_off()

    def update(frame):
        image = np.ones((100, 300), dtype=np.uint8) * 100  # gray background

        # Simulate different tissue densities (0-255)
        bone_intensity = 255  # High attenuation (bright)
        muscle_intensity = 150  # Moderate attenuation (gray)
        air_intensity = 50   # Low attenuation (dark)

        # Draw shapes with different intensities
        cv2.circle(image, (75, 50), 30, bone_intensity, -1) #Bone
        cv2.circle(image, (225, 50), 30, muscle_intensity, -1) #Muscle
        cv2.rectangle(image, (140, 20), (160, 80), air_intensity, -1) #Air

        ax.imshow(image, cmap='gray')
        ax.set_title(f"Simulated X-ray Attenuation")
        return ax,

    ani = animation.FuncAnimation(fig, update, frames=10, blit=True, repeat=False)
    return ani

def main():
    st.title("Simulating X-ray Attenuation")

    st.markdown("""
    **X-ray Attenuation Simulation**

    Different tissues absorb X-rays at different rates, which is the principle behind X-ray imaging. This simulation visualizes how varying tissue densities affect X-ray absorption.

    *   **High attenuation materials (e.g., bone)** absorb more X-rays and appear **brighter** on an X-ray image.
    *   **Low attenuation materials (e.g., air)** allow more X-rays to pass through and appear **darker**.
    *   **Intermediate tissues (e.g., muscle)** absorb X-rays to a moderate degree and appear in shades of **gray**.

    **Biological Interpretation:**

    *   Bones appear bright white due to their high calcium content and density.
    *   Lungs, being mostly air-filled, appear dark, aiding in the detection of infiltrates.
    *   Soft tissues like organs appear in varying shades of gray based on their composition.
    """)

    ani = generate_animation()
    st.pyplot(ani)

if __name__ == "__main__":
    main()