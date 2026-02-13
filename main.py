import json
import os
from config import FOLDER_WITH_DATA, OUTPUT_PATH, OUTPUT_FILE_NAME,JSON_VERSION
from pathlib import Path

def main():
    lookup = {}
    print("[INFO] Searching for files...")
    for file in os.listdir(FOLDER_WITH_DATA):
        
        file_path = Path(FOLDER_WITH_DATA, file)
        if file_path.suffix.lower() != ".json":
            continue
        print(f"[INFO] Found {file}.")
        
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