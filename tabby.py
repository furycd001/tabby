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
    parser.add_argument("sessionstore_dir", help="Path to your sessionstore-backups directory")
    parser.add_argument("session_file", help="Name of the session file to extract from (e.g., previous.jsonlz4)")

    args = parser.parse_args()

    # Construct the full path to the session file
    session_file = os.path.join(args.sessionstore_dir, args.session_file)

    # Decompress the session file
    decompressed_data = decompress_jsonlz4(session_file)

    # Extract URLs from the decompressed JSON data
    urls = extract_urls(decompressed_data.decode('utf-8'))

    # Print the URLs
    for url in urls:
        print(url)

if __name__ == "__main__":
    main()