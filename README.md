# Korean-audio-to-text-clova
"Converts Korean audio files to text using the Clova Speech-to-Text API. Processes audio from the Korean Single Speaker Speech Dataset and outputs transcriptions to a CSV file."

# Audio to Text Conversion using Clova API

This project converts Korean audio files to text using the Clova Speech-to-Text API. It processes audio files from the Korean Single Speaker Speech Dataset and outputs the transcriptions in a CSV file. Only audio files from the first subfolder (alphabetically sorted) of the dataset's `kss` directory are processed.

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


