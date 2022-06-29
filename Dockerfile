# Base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Set working directory
WORKDIR /churn_project

# Copy files
COPY main.py /churn_project
COPY requirements_dev.txt /churn_project
COPY model /churn_project/model
COPY ms /churn_project/ms
COPY api_tests.py /churn_project

# Install dependencies
RUN pip install -r requirements_dev.txt

# Run the application
EXPOSE 8000
CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8000"]
