# Word Correction Project

This project implements a simple word correction tool using the Levenshtein distance algorithm and Streamlit for the user interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 3.7 or later
* You have installed the required packages (see Installation section)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Phatban/Streamlit-AI-Projects.git
   cd Word_Correction
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
3. Download the vocabulary file:
- Download the `vocab.txt` file from [this link](https://drive.google.com/file/d/1Kfl1a1rmIebcGK7dWvBWgbOoMI89fDzO/view?usp=drive_link)
- Place the downloaded `vocab.txt` file in the project directory

## Usage

To run the Word Correction application:

1. Ensure you are in the project directory
2. Run the following command:
   ```bash
   streamlit run main.py
4. Open your web browser and go to the URL displayed in the terminal (usually http://localhost:8501)

## How it works

1. The application loads a vocabulary from the `vocab.txt` file
2. Enter a word in the text input field
3. Click the "Compute" button
4. The application will display the closest matching word from the vocabulary based on the Levenshtein distance

## Project Structure

- `main.py`: Contains the Streamlit user interface and main application logic
- `levenshtein_distance.py`: Implements the Levenshtein distance algorithm and word finding function
- `vocab.txt`: Contains the vocabulary words (needs to be downloaded separately)
- `requirements.txt`: Lists the Python packages required for this project

## Contributing

Contributions to this project are welcome. Please ensure you follow the coding style and add unit tests for any new features.


