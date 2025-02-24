import os
import requests
import csv

# Clova API credentials (replace with your own)
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

# Language code for Korean
lang = "Kor"
# Clova API URL
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang

# Root directory for the 'kss' folder (containing multiple subfolders)
root_directory = "/content/korean-single-speaker-speech-dataset/kss"

# Get list of subfolders and select the first one (alphabetically sorted)
subfolders = sorted([f for f in os.listdir(root_directory) if os.path.isdir(os.path.join(root_directory, f))])
if not subfolders:
    print("No subfolders found in", root_directory)
else:
    first_folder = subfolders[0]
    target_directory = os.path.join(root_directory, first_folder)
    print("Processing audio files from folder:", target_directory)

results = []  # List to store results as (file_number, text)
file_number = 1

# Process audio files in the selected folder
for foldername, subfolders, filenames in os.walk(target_directory):
    for filename in filenames:
        if filename.endswith(".wav"):
            file_path = os.path.join(foldername, filename)
            print(f"Processing file: {file_path}")

            with open(file_path, 'rb') as data:
                headers = {
                    "X-NCP-APIGW-API-KEY-ID": client_id,
                    "X-NCP-APIGW-API-KEY": client_secret,
                    "Content-Type": "application/octet-stream"
                }
                response = requests.post(url, data=data, headers=headers)

                if response.status_code == 200:
                    text_result = response.text
                    results.append((file_number, text_result))
                    print(f"File {file_number}: Transcription successful.")
                else:
                    print(f"Error processing {file_path}: {response.text}")
            file_number += 1

# Save results to a CSV file
csv_file = "/content/audio_transcriptions.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["file_number", "text"])
    writer.writerows(results)

print("CSV file created at:", csv_file)

