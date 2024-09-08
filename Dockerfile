# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and SQLAlchemy
RUN pip install flask flask-sqlalchemy

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
