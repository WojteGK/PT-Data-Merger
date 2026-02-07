import json
import os
import pprint
from config import FOLDER_WITH_DATA
from pathlib import Path
from mergedeep import merge, Strategy

def main():
    files_to_merge = []
    for file in os.listdir(FOLDER_WITH_DATA):
        with open(Path(FOLDER_WITH_DATA, file), "r") as f:
            files_to_merge.append(json.load(f))

    output = files_to_merge.pop(-1)
    output = merge(output, *files_to_merge, strategy=Strategy.ADDITIVE)
    pprint.pprint(output)

if __name__ == "__main__":
    main()
