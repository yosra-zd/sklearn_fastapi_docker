# Base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Set working directory
WORKDIR /churn_project/test

# Copy files
COPY . /churn_project
 
# Install dependencies
#RUN pip install -r requirements.txt

# Run the application
EXPOSE 9000 
CMD python3 /churn_project/test/api_tests.py
