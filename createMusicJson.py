import os
import json

def create_url_json(folder_path, base_url):
    # Get all files with .m4a extension in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.m4a')]
    
    # Extract folder name from the path
    folder_name = os.path.basename(folder_path)
    
    # Create the URLs list
    urls = []
    for file in files:
        # Remove the .m4a extension for the URL
        file_name = os.path.splitext(file)[0]
        url = f"{base_url}/{folder_name}/{file_name}.m4a"
        urls.append(url)
    
    # Create the JSON structure
    json_data = {
        "files": urls
    }
    
    # Write to JSON file
    output_file = f"{folder_name}/music.json"
    with open(output_file, 'w') as f:
        json.dump(json_data, f, indent=2)
    
    print(f"Created {output_file} with {len(urls)} URLs")

# Example usage
base_url = "https://ahilan-subbaian.github.io/NFCmessage"
folder_path = "srinidhi"  # Replace with your folder path
create_url_json(folder_path, base_url)