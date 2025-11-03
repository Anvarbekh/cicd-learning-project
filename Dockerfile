# Start from a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /code

# Copy the dependencies file and install them
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code into the container
COPY ./app /code/app

# Tell Docker what command to run when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]