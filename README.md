# Audio to Text Conversion using Clova API

This project converts Korean audio files to text using the Clova Speech-to-Text API. It processes audio files from the Korean Single Speaker Speech Dataset and outputs the transcriptions in a CSV file.

## Features

- **Audio Processing:** Automatically traverse the designated folder to locate and process `.wav` files.
- **Speech-to-Text Conversion:** Send audio files to the Clova API to obtain text transcriptions.
- **Output Storage:** Save the transcription results in a CSV file (`audio_transcriptions.csv`) containing two columns: `file_number` and `text`.

## Prerequisites

- A Python environment (e.g., Google Colab)
- Clova API credentials (client_id and client_secret obtained from Naver Cloud)
- The Korean Single Speaker Speech Dataset must be available at `/content/korean-single-speaker-speech-dataset/kss`
- Required Python libraries: `os`, `requests`, and `csv`

## Project Structure
- **README.md:** Contains the project description, setup instructions, usage details, and project structure.
- **main.py:** The main Python script that processes audio files, converts them to text via the Clova API, and writes the results to a CSV file.
- **requirements.txt:** Lists the Python packages required to run the project.
- **.gitignore:** Specifies files and directories that should not be committed to GitHub (e.g., temporary files or generated outputs).

1. **Clova API Setup:**  
   Replace the `client_id` and `client_secret` in the `main.py` file with your actual Clova API credentials.

2. **Dataset Location:**  
   Ensure that the Korean Single Speaker Speech Dataset is extracted and available at the following path:  
   `/content/korean-single-speaker-speech-dataset/kss`  
   The dataset is expected to have multiple subfolders inside `kss`, and only the first subfolder (alphabetically) will be processed.

3. **Install Required Libraries:**  
   Install the necessary Python packages. For example, if you are using Google Colab, you can run:


