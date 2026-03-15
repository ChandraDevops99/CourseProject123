# Dockerfile
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Make wait_for_db.py executable
RUN chmod +x wait_for_db.py

# Command to wait for DB and run server
CMD ["python", "wait_for_db.py", "python", "manage.py", "runserver", "0.0.0.0:8000"]