# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file first to install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app folder into the container
COPY . .

# Expose the port Flask runs on (default 5000)
EXPOSE 5000

# Define the command to run the application
CMD ["python", "run.py"]