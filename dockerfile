# Use an official Python image as the base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install youtube-transcript-api


# Copy the rest of the application files
COPY . .

# Default command (optional, modify as needed)
CMD ["python", "program.py"]


