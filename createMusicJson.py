import os
import json
import sys

def create_url_json(folder_name, base_url="https://ahilan-subbaian.github.io/NFCmessage"):
    # Get the absolute path to the folder
    folder_path = os.path.join(os.getcwd(), folder_name)
    
    # Only process audio files in the folder
    audio_extensions = ('.m4a', '.mp3', '.wav', '.ogg', '.aac')
    files = [f for f in os.listdir(folder_path) if f.endswith(audio_extensions)]
    
    if not files:
        print(f"No audio files found in folder: {folder_name}")
        return
    
    urls = []
    for file in files:
        file_name, ext = os.path.splitext(file)
        url = f"{base_url}/{folder_name}/{file_name}{ext}"
        urls.append(url)
        
    json_data = {"files": urls}
    
    # Ensure the music.json file is written to the correct folder path
    output_file = os.path.join(folder_path, "music.json")
    
    # Write to the file
    with open(output_file, 'w') as f:
        json.dump(json_data, f, indent=2)
    
    print(f"Created {output_file} with {len(urls)} URLs")

if __name__ == "__main__":
    folder_name = sys.argv[1]  # The folder name passed as argument
    base_url = sys.argv[2] if len(sys.argv) > 2 else "https://ahilan-subbaian.github.io/NFCmessage"
    create_url_json(folder_name, base_url)
