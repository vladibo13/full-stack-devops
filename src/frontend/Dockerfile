# Use Node.js for both build and runtime stages
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app's source code
COPY . .

# Build the React app for production
RUN npm run build

# Install `serve` to serve the build output
RUN npm install -g serve

# Expose the port on which the app will run
EXPOSE 3000

# Start the React app using `serve`
CMD ["serve", "-s", "build", "-l", "3000"]