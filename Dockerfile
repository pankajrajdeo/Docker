# Use an official Alpine Linux as a parent image
FROM alpine:latest

# Install Python
RUN apk add --update python3 py3-pip

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run script.py when the container launches
CMD ["python3", "script.py"]
