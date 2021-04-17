# We Use an official Python runtime as a parent image
FROM python:3.7

# Set working directory
WORKDIR /code

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY requirements.txt /code/
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y libpq-dev  \
    gcc \
    postgresql-client

# Mounts the application code to the image
COPY . /code/

# EXPOSE 8000

# # runs the production server
# ENTRYPOINT ["python", "manage.py"]
# CMD ["runserver", "0.0.0.0:8000"]