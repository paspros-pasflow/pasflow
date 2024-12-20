# Introduction

Welcome to the AI-Powered Task Automation Solution! This application leverages NVIDIA Triton Inference Server to automate tasks, optimize workflows, and improve productivity by providing AI-based predictions for task assignments and performance tracking.

## Key Features:
- Real-Time Task Automation using AI.
- Seamless Integration with NVIDIA Triton Inference Server for optimized performance.
- Scalable and Efficient architecture suitable for enterprise applications.

## SDK Integration

## Prerequisites
Before integrating the NVIDIA Triton Inference Server SDK into your project, ensure that the following are set up:

Hardware Requirements:

- NVIDIA GPU with CUDA support.
- NVIDIA Triton Inference Server requires CUDA 11.2 or higher.
  
Software Requirements:

  - Python 3.8 or higher.
  - Flask or any Python web framework (if building a web application).
  - NVIDIA Triton SDK for Python integration.
  
Dependencies:

  - Install the following Python libraries:
  ` pip install tritonclient[http]flask numpy`

# Installation Steps

Clone the repository:

`git clone https://github.com/your-repository/ai-task-automation.git`

`cd ai-task-automation`


Set up the NVIDIA Triton Inference Server:

- Docker Deployment (Recommended):
Pull the Triton Docker image:

docker pull nvcr.io/nvidia/tritonserver:23.01-py3`

- Run Triton Server:
  
`docker run --gpus all -d --rm -p 8000:8000 -p 8001:8001 -p 8002:8002 --name triton_server nvcr.io/nvidia/tritonserver:23.01-py3 tritonserver --model-repository=/models`


- Manual Installation:
  
Follow the installation instructions on the Triton Inference Server GitHub.

- Install the required Python dependencies:
- 
In the root directory of the project, create a requirements.txt and add:

`tritonclient[http]==2.37.0`
`flask==3.0.0`
`numpy==1.26.0`

Install the dependencies:

`pip install -r requirements.txt



# Configuration

Model Deployment:
Place your model files in the specified model repository directory (`/models/task_classification_model/1/model.pt`), and ensure the model is ready for deployment.



# Setup Instructions

1.Running the Application

Start Triton Inference Server:
If you're using Docker:

`docker run --gpus all -d --rm -p 8000:8000 -p 8001:8001 -p 8002:8002 --name triton_server nvcr.io/nvidia/tritonserver:23.01-py3 tritonserver --model-repository=/path/to/your/model-repository`

2.Start the Flask Web Application:
Run the Flask application:

`python app.py`


This will start a local server at `http://localhost:5000.

3.Verify the Server:
Open a web browser and go to http://localhost:5000 to access the application. You can use the /predict endpoint to send data for task automation predictions.



# Usage

Making Predictions

- Endpoint: /predict
- Method: POST
- Request Body:
The input data should be a JSON object with the task features.

- Response:
The response will return the predicted task automation outcome.
Example:



