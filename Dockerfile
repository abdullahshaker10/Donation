# Base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose port
EXPOSE 8004

# Copy entrypoint script
COPY entrypoint.sh /app/entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["sh", "/app/entrypoint.sh"]