# Pull Base Image
FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Install dependencies
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system --deploy

# Copy project
COPY . /app/

# Expose port
EXPOSE 9696

# For heroku, we cannot map to a custom port so the binding
# ENTRYPOINT ["gunicorn", "predict:app"]

# For any other way of use
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]