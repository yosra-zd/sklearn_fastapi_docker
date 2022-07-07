# Base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Set working directory
WORKDIR /churn_project/test

# Copy files
COPY churn_project/test /churn_project/test
 
# Install dependencies
RUN pip install -r requirements.txt

# Run the application
EXPOSE 8000
CMD python3 api_tests.py
