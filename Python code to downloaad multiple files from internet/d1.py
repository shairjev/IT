import requests

def download_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully to {destination}")
    else:
        print(f"Failed to download file from {url}. Status code:{response.status_code}")
# List of URLs to download from
urls_to_download = [
"https://results.kongu.edu/Photos/22CHL088.JPG",
"https://results.kongu.edu/Photos/22CHR041.JPG",
"https://results.kongu.edu/Photos/22EIR052.JPG",
"https://results.kongu.edu/Photos/22AUL038.JPG",
"https://results.kongu.edu/Photos/22AUL036.JPG",
"https://results.kongu.edu/Photos/22AUL044.JPG",
"https://results.kongu.edu/Photos/22MTR058.JPG",
"https://results.kongu.edu/Photos/22EEL129.JPG",
"https://results.kongu.edu/Photos/22EEL117.JPG",
"https://results.kongu.edu/Photos/22ALL120.JPG",
"https://results.kongu.edu/Photos/22CSL245.JPG",
"https://results.kongu.edu/Photos/22ECL253.JPG",
"https://results.kongu.edu/Photos/22ECL263.JPG",
"https://results.kongu.edu/Photos/22ADR011.JPG",
"https://results.kongu.edu/Photos/22CHL090.JPG",
"https://results.kongu.edu/Photos/22CHL085.JPG",
"https://results.kongu.edu/Photos/22CHL087.JPG",
"https://results.kongu.edu/Photos/22MTR074.JPG",
"https://results.kongu.edu/Photos/22ECL268.JPG",
"https://results.kongu.edu/Photos/22MTL123.JPG",
"https://results.kongu.edu/Photos/22ADL128.JPG",
"https://results.kongu.edu/Photos/22CSL263.JPG",
"https://results.kongu.edu/Photos/22EIL114.JPG",
"https://results.kongu.edu/Photos/22CEL086.JPG",
"https://results.kongu.edu/Photos/22CSR236.JPG"
]

# Destination directory where files will be saved
destination_directory = "downloaded_files"

# Create the destination directory if it doesn't exist
import os
os.makedirs(destination_directory, exist_ok=True)

# Download files from each URL in the list
for url in urls_to_download:
    # Extract filename from the URL
    filename = url.split("/")[-1]
    # Construct the full destination path
    destination_path = os.path.join(destination_directory, filename)
    
    # Download the file
    download_file(url, destination_path)

