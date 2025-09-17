# Use Python 3.11 as base image
FROM python:3.11

# Set working directory inside container
WORKDIR /app

# Copy requirements and install packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all project files
COPY . .

# Run Flask app
CMD ["python", "app.py"]
