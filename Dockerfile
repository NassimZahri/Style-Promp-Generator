# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install build dependencies and clean up after installing Python packages
RUN apt-get update && apt-get install -y build-essential && \
	pip install --no-cache-dir -r requirements.txt && \
	apt-get remove -y build-essential && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

# Expose port 5000 for Flask
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=src/app.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]