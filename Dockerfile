FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install OpenGL dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib20-0 \
    mesa-utils \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for OpenGL
ENV DISPLAY=:99
ENV LIBGL_ALWAYS_INDIRECT=1

COPY . .

CMD ["streamlit", "run", "streamlit_app.py"]