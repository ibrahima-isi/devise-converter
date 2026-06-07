# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies needed for PySide6 and GUI display
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libxrender1 \
    libxext6 \
    libfontconfig1 \
    libxi6 \
    libxrandr2 \
    libxcursor1 \
    libxcomposite1 \
    libxdamage1 \
    libpango-1.0-0 \
    libatk1.0-0 \
    libc6 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libexpat1 \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy application code
COPY app/ ./app/

# Expose any necessary ports (not needed for GUI app, but keeping for completeness)
# EXPOSE 8080

# Set environment variables for display (will be overridden at runtime)
ENV DISPLAY=:0

# Run the application
CMD ["python", "app/app.py"]