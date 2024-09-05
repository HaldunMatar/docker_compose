
FROM mysql:latest

RUN apt-get update && apt-get install -y
RUN mysql -e "CREATE DATABASE madb;"
RUN mysql -e "CREATE USER 'dba'@'%' IDENTIFIED BY 'Password123$';"
RUN mysql -e "GRANT ALL PRIVILEGES ON madb.* TO 'dba'@'%';"
COPY script.sql /docker-entrypoint-initdb.d/
EXPOSE 3306


# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV HOST_NAME="your_default_hostname"
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install required system packages for OpenCV, GLib, tkinter, and iproute2
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    python3-tk \
    iproute2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*



COPY requirements.txt /app/

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
#run pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# Copy the entire project directory into the container
COPY . /app

# Expose the necessary ports
EXPOSE 5005
EXPOSE 3306

# Command to run your application
CMD ["python3", "main.py"]
