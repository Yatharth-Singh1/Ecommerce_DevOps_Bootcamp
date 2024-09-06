# Use a base image with Python and Flask pre-installed
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code to the container
COPY . .

# Expose the port on which the Flask app will run (default is 5000)
EXPOSE 8080

# Set the environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Set the command to run the Flask app when the container starts
CMD ["python", "app.py"]
