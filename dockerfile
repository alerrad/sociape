FROM node:16-alpine AS builder

# Build the front-end
WORKDIR /app/client
COPY package.json .
RUN npm install
COPY --from=0 /app/client/node_modules ./node_modules
RUN npm run build

# Build the back-end
WORKDIR /app/server
COPY package.json .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV MONGO_URI=mongodb://localhost:27017
ENV SECRET_SALT=your_sercret_salt

# Create the main image
FROM nginx:stable-alpine

WORKDIR /app

# Copy the built front-end
COPY --from=builder /app/client/build ./build

# Copy the back-end application
COPY --from=builder /app/server/app ./app

# Configure Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 3000
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]