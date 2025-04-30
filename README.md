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

## Setup and Execution

1. **Clova API Setup:**  
   Replace the `client_id` and `client_secret` in the `main.py` file with your actual Clova API credentials.

2. **Creating and Configuring Clova API:**  
   - Log in to your Naver Cloud Platform account.
   - Navigate to the API section and create a new Clova Speech-to-Text API instance.
   - Follow the provided instructions to obtain your `client_id` and `client_secret`.
   - Make sure to review the usage policies and rate limits.
  
   - https://api.ncloud-docs.com/docs/ai-application-service-clovaspeech

3. **Dataset Location:**  
   Ensure that the Korean Single Speaker Speech Dataset is extracted and available at:  
   `/content/korean-single-speaker-speech-dataset/kss`  
   The dataset should have multiple subfolders inside `kss`, and only the first subfolder (alphabetically) will be processed.

4. **Install Required Libraries:**  


5. **Run the Code:**  
Execute the `main.py` script. The script will:
- Traverse the first subfolder inside `/content/korean-single-speaker-speech-dataset/kss`
- Process each `.wav` file by sending it to the Clova API for transcription
- Save the transcriptions along with a file number in `audio_transcriptions.csv`

## Additional Notes

- **API Rate Limits:**  
The Clova API has request rate limits. If processing a large number of files, consider adding delays or retry logic to handle rate-limiting issues.

- **Error Handling:**  
Errors during processing are printed to the console. You can enhance the error handling for more robust behavior if needed.

## License

This project is provided for educational and research purposes only. Please adhere to the usage policies of the Clova API and the dataset.

## Additional Notes

- **API Rate Limits:**  
The Clova API has request rate limits. If processing a large number of files, consider adding delays or retry logic to handle rate-limiting issues.

- **Error Handling:**  
Errors during processing are printed to the console. You can enhance the error handling for more robust behavior if needed.

## License

This project is provided for educational and research purposes only. Please adhere to the usage policies of the Clova API and the dataset.




## 📌 기술 평가 항목 대응 내역

본 프로젝트는 Python을 활용하여 한국어 음성 데이터를 Clova Speech-to-Text API를 통해 텍스트로 자동 변환하고, 결과를 CSV 파일로 저장하는 자동화 파이프라인을 구현하였습니다. 다음의 기술 항목을 포함합니다:

- **[1. 데이터사이언스 공통]**  
  `os`, `csv`, `requests` 라이브러리를 사용하여 음성 파일 탐색, API 통신, 결과 저장을 자동화하였습니다.

- **[3. 데이터 수집 및 정제]**  
  Clova Open API를 사용하여 `.wav` 파일을 전송하고, 응답받은 텍스트를 정제하여 저장하였습니다. 
  변환된 텍스트는 `audio_transcriptions.csv` 형식으로 저장되어 후속 분석 및 자연어처리에 활용할 수 있습니다.





   
