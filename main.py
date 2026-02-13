import json
import os
from config import FOLDER_WITH_DATA, OUTPUT_PATH, OUTPUT_FILE_NAME,JSON_VERSION
from pathlib import Path

def main():
    if not os.path.exists(FOLDER_WITH_DATA):
        print(f"[WARN] Directory {Path(FOLDER_WITH_DATA).absolute()} doesn't exist. Creating...")
        os.makedirs(FOLDER_WITH_DATA)
    if not os.listdir(FOLDER_WITH_DATA):
        print(f"[ERROR] Directory is empty. Please insert .json files into \
              {Path(FOLDER_WITH_DATA).absolute()} or change data path in config.")
    if not os.listdir(OUTPUT_PATH):
        print("[WARN] Output path doesn't exist. Creating...")
        os.makedirs(OUTPUT_PATH)

    lookup = {}
    print("[INFO] Searching for files...")
    for file in os.listdir(FOLDER_WITH_DATA):
        
        file_path = Path(FOLDER_WITH_DATA, file)
        if file_path.suffix.lower() != ".json":
            continue
        print(f"[INFO] Found {file}. Processing...")
        
        raw_data = None
        with open(file_path, "r") as f:
            raw_data = json.load(f)

        for info in raw_data['ProspectInfos']:
            coord_key = (info['Chunk']['X'], info['Chunk']['Z'])
            if coord_key not in lookup:
                lookup[coord_key] = info
            else:
                print(f'[WARN] duplicated chunk: [X:{coord_key[0]}, Z:{coord_key[1]}]. Skipping...')

    new_prospect_infos = list(lookup.values())
    final_json = {'Version': JSON_VERSION, 'ProspectInfos': new_prospect_infos}

    with open(Path(OUTPUT_PATH, OUTPUT_FILE_NAME), mode="w") as writer:
        writer.write(json.dumps(final_json, separators=(',', ':')))
    print(f"[INFO] Success! File saved to: {Path(OUTPUT_PATH).absolute()} as {OUTPUT_FILE_NAME}")

if __name__ == "__main__":
    main()