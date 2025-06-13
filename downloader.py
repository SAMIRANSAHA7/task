import os
import zipfile
import requests
from io import BytesIO

def download_and_extract_medquad(destination="../data"):
    url = "https://github.com/abachaa/MedQuAD/archive/refs/heads/master.zip"
    print("📥 Downloading MedQuAD dataset...")
    response = requests.get(url)
    if response.status_code == 200:
        with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(destination)
        print("✅ Dataset downloaded and extracted.")
    else:
        print("❌ Failed to download. Check the URL or your internet connection.")

if __name__ == "__main__":
    os.makedirs("../data", exist_ok=True)
    download_and_extract_medquad()
