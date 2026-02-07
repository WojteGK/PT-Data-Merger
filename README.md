# PT Data Merger

## Running:
0. Adjust `config.py` if needed 
1. Install uv: [Official installation site](https://docs.astral.sh/uv/getting-started/installation/)
2. Run `uv run main.py`. The tool will handle .venv and deps by itself

## Config
`FOLDER_WITH_DATA` - a path to the folder with .json files that should be merged.
`OUTPUT_PATH` - a path to the folder where the output .json will be placed. Please adjust permissions so the program can actually write data inside.

## Warning
Currently the script won't handle duplicates. Be aware of this while using it.