# PT Data Merger
## About
This script was created as a tool for Vintage Story mod named "Prospect Together". The tools' purpose is to merge several .json files (from different players) into one that contains all prospecting information.
    [Prospect Together mod site](https://mods.vintagestory.at/prospecttogether) 
    [Vintage Story official site](https://www.vintagestory.at/)

## Running:
0. Adjust `config.py` if needed 
1. Install uv: [Official installation site](https://docs.astral.sh/uv/getting-started/installation/)
2. Run `uv run main.py`. The tool will handle .venv and deps by itself

## Config
`FOLDER_WITH_DATA` - a path to the folder with .json files that should be merged. Default: `"./data"`
`OUTPUT_PATH` - a path to the folder where the output .json will be placed. Please adjust permissions so the program can actually write data inside. Default: `"./output"`
`OUTPUT_FILE_NAME` - Name of the output file. Leave default unless you know what you're doing. Default: `"prospectTogetherClient.json"`
`JSON_VERSION` - Version of the json file. Leave default unless you know what you're doing. Default: `1`

## About