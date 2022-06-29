# Base image
FROM python:3.10

# Set working directory
WORKDIR /churn_project

# Copy files
COPY main.py /churn_project
COPY requirements_dev.txt /churn_project
COPY model /churn_project/model
COPY ms /churn_project/ms

# Install dependencies
RUN pip install -r requirements_dev.txt

# Run the application
EXPOSE 8000
CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8000"]
