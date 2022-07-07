# Base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Set working directory
WORKDIR /churn_project

# Copy files
COPY . /churn_project
 
# Install dependencies
RUN python -m pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt

# Run the application
EXPOSE 8000
CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8000"]
