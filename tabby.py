import json
import lz4.block
import os
import argparse

def decompress_jsonlz4(file_path):
    with open(file_path, 'rb') as f:
        magic = f.read(8)  # First 8 bytes are the magic number
        compressed_data = f.read()
    return lz4.block.decompress(compressed_data)

def extract_urls(json_data):
    urls = []
    data = json.loads(json_data)
    for window in data.get('windows', []):
        for tab in window.get('tabs', []):
            for entry in tab.get('entries', []):
                urls.append(entry.get('url'))
    return urls

def main():
    parser = argparse.ArgumentParser(description="Extract URLs from Firefox sessionstore files.")
    parser.add_argument('sessionstore_dir', help="Path to the sessionstore-backups directory.")
    args = parser.parse_args()

    sessionstore_dir = args.sessionstore_dir

    # Automatically select the latest session file
    session_files = [f for f in os.listdir(sessionstore_dir) if f.endswith('.jsonlz4')]
    if not session_files:
        print("No .jsonlz4 files found in the directory.")
        return

    session_file = os.path.join(sessionstore_dir, max(session_files, key=lambda f: os.path.getmtime(os.path.join(sessionstore_dir, f))))

    # Decompress the session file
    decompressed_data = decompress_jsonlz4(session_file)

    # Extract URLs from the decompressed JSON data
    urls = extract_urls(decompressed_data.decode('utf-8'))

    # Print the URLs
    for url in urls:
        print(url)

if __name__ == "__main__":
    main()
