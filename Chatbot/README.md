# Chatbot Project

This project implements a simple chatbot using the HugChat library and Streamlit for the user interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 3.7 or later
* You have installed the required packages (see Installation section)
* You have a Hugging Face account with access to HugChat

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Phatban/Streamlit-AI-Projects.git
   cd Chatbot
2. Install the required packages:
   ```bash
   pip install -r requirements.txt

## Usage

To run the Chatbot application:

1. Ensure you are in the project directory
2. Run the following command:
   ```bash
   streamlit run main.py
3. Open your web browser and go to the URL displayed in the terminal (usually http://localhost:8501)
4. Enter your Hugging Face credentials when prompted

## How it works

1. The application asks for your Hugging Face credentials
2. Once authenticated, you can start chatting with the bot
3. The chatbot uses the HugChat model to generate responses

## Project Structure

- `main.py`: Contains the Streamlit user interface and main application logic
- `chatbot.py`: Implements the chatbot functionality using HugChat
- `requirements.txt`: Lists the Python packages required for this project

## Contributing

Contributions to this project are welcome. Please ensure you follow the coding style and add unit tests for any new features.
