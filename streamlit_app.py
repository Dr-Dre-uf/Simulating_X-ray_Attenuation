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

        # Simulate different tissue types with varying attenuation
        # Dark circle: Low attenuation (like air or fat)
        cv2.circle(image, (75 + frame * 5, 50), 30, 30, -1)
        # Bright rectangle: High attenuation (like bone)
        cv2.rectangle(image, (140 - frame * 2, 20), (160 + frame * 2, 80), 200, -1)
        # Gray circle: Intermediate attenuation (like muscle)
        cv2.circle(image, (225 - frame * 5, 50), 30, 100, -1)  # Intermediate gray value

        ax.imshow(image, cmap='gray')
        ax.set_title(f"Simulated X-ray Attenuation (Frame {frame + 1})")
        return ax,

    ani = animation.FuncAnimation(fig, update, frames=20, blit=True, repeat=False)
    return fig

def main():
    st.title("Simulating X-ray Attenuation")

    st.write("""
    This app simulates how different tissues absorb X-rays.  X-rays pass through the body and are attenuated (absorbed) to varying degrees depending on the tissue's density and composition.  

    **Key Concepts:**

    *   **Attenuation:** The reduction in X-ray intensity as it passes through a material.
    *   **Tissue Contrast:** The difference in X-ray attenuation between different tissues.
    *   **Brighter Regions:**  Materials that absorb more X-rays (high attenuation) appear brighter on an X-ray image. (e.g., Bone)
    *   **Darker Regions:** Materials that allow more X-rays to pass through (low attenuation) appear darker. (e.g., Air in lungs)
    """)

    st.subheader("Simulation")
    fig = generate_animation()
    st.pyplot(fig)

    st.subheader("Interpretation")
    st.write("""
    In the simulation:

    *   The **dark circle** represents a tissue with *low* attenuation (like air or fat).
    *   The **bright rectangle** represents a tissue with *high* attenuation (like bone).
    *   The **gray circle** represents a tissue with *intermediate* attenuation (like muscle).
    
    Observe how these different attenuation levels create contrast in the image.
    
    **Biological Relevance:**

    *   Bones appear bright white due to their high calcium content and density.
    *   Lungs appear dark because they are filled with air.
    *   Soft tissues such as muscles, organs, and fat appear in shades of gray. 
    """)

if __name__ == "__main__":
    main()