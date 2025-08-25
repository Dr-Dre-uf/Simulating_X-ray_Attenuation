import streamlit as st
import numpy as np

# Create the image as a NumPy array
image_data = np.ones((100, 300), dtype=np.uint8) * 100  # Gray background

# Simulate dark spots (using lower values for darker areas)
image_data[40:70, 65:95] = 0  # Dark spot 1
image_data[40:70, 215:245] = 0  # Dark spot 2

# Simulate white rectangle (using higher values for brighter areas)
image_data[10:90, 130:160] = 200

# Display the image in Streamlit
st.image(image_data, caption="Simulated X-ray Attenuation", channels="GRAY")