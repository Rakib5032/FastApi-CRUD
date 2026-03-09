# Use an official lightweight Python image
FROM python:3.11-slim

# Set environment variables to optimize Python for containers
# Prevents Python from writing .pyc files and keeps logs flushing to the terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (only if needed by specific libraries)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first to leverage Docker's layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application using Uvicorn
# 0.0.0.0 is necessary to allow external access to the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]