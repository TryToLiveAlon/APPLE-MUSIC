# Use a base image with Python 3.10 and Node.js 19
FROM nikolaik/python-nodejs:python3.10-nodejs19

# Install dependencies (ffmpeg for audio, aria2 for downloading)
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg aria2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY . /app/

# Set the working directory
WORKDIR /app/

# Upgrade pip and install Python dependencies
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir --requirement requirements.txt

# Run the bot
CMD ["python3", "-m", "VIPMUSIC"]
