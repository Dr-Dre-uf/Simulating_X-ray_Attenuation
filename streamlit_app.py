import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Create the image
image = np.ones((100, 300), dtype=np.uint8) * 100  # gray background

# Add circular spots
cv2.circle(image, (75, 50), 30, 0, -1)  # dark spot
cv2.circle(image, (225, 50), 30, 0, -1)  # dark spot

# Add white rectangle
cv2.rectangle(image, (140, 20), (160, 80), 200, -1)

# Display the image in Streamlit
st.image(image, caption="Simulated X-ray Attenuation", channels="GRAY")
