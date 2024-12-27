import os
import json
import sys

def create_url_json(folder_path, base_url="https://ahilan-subbaian.github.io/NFCmessage"):
    audio_extensions = ('.m4a', '.mp3')
    files = [f for f in os.listdir(folder_path) if f.endswith(audio_extensions)]
    folder_name = os.path.basename(folder_path)
    
    urls = []
    for file in files:
        file_name, ext = os.path.splitext(file)
        url = f"{base_url}/{folder_name}/{file_name}{ext}"
        urls.append(url)
        
    json_data = {"files": urls}
    output_file = f"{folder_name}/music.json"
    
    with open(output_file, 'w') as f:
        json.dump(json_data, f, indent=2)
    print(f"Created {output_file} with {len(urls)} URLs")

if __name__ == "__main__":
    folder_path = sys.argv[1]
    base_url = sys.argv[2] if len(sys.argv) > 2 else "https://ahilan-subbaian.github.io/NFCmessage"
    create_url_json(folder_path, base_url)