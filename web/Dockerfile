# Pull official base image
FROM python:3.8.3-slim-buster

# Set working directory
WORKDIR /usr/src/app

# Copy web appliction files
COPY . /usr/src/app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements

# Run server
CMD gunicorn --bind :5000 wsgi:app