# Object Detection Project

This project implements a simple object detection tool using OpenCV's DNN module and Streamlit for the user interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 3.7 or later
* You have installed the required packages (see Installation section)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Phatban/Streamlit-AI-Projects.git
   cd Object_Detection
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
3. Download the model files:
- Download the `MobileNetSSD_deploy.caffemodel` and `MobileNetSSD_deploy.prototxt.txt` files from [this link](https://example.com/path-to-your-model-files)
- Place the downloaded files in the `model` directory

## Usage

To run the Object Detection application:

1. Ensure you are in the project directory
2. Run the following command:
   ```bash
   streamlit run main.py
3. Open your web browser and go to the URL displayed in the terminal (usually http://localhost:8501)

## How it works

1. Upload an image through the Streamlit interface
2. The application processes the image using the pre-trained MobileNet-SSD model
3. Detected objects are highlighted in the output image

## Project Structure

- `main.py`: Contains the Streamlit user interface and main application logic
- `object_detection.py`: Implements the object detection functions using OpenCV
- `model/`: Directory containing the pre-trained model files
- `requirements.txt`: Lists the Python packages required for this project

## Contributing

Contributions to this project are welcome. Please ensure you follow the coding style and add unit tests for any new features.
