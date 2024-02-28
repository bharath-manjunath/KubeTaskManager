# Use the official Node.js image as the base image for building the frontend
FROM node:14 AS frontend-builder

WORKDIR /app

# Copy frontend dependencies and build the frontend
RUN apt update && apt install npm
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Use the official Python image as the base image
FROM python:3.9

WORKDIR /app

# Copy backend dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Copy the built frontend files from the frontend-builder image
COPY --from=frontend-builder /app/build /app/frontend/build
RUN apt install sqlite3
# Expose the ports
EXPOSE 5000 
EXPOSE 3000  

# Specify the command to run on container startup
CMD ["sh", "-c", "python app.py && npm start --prefix frontend"]
