import os
from pathlib import Path

# Get the root directory of the project
ROOT_DIR = Path(__file__).parent.parent.parent.parent

# Define paths relative to root
CONFIG_FILE_PATH = ROOT_DIR / "config/config.yaml"
PARAMS_FILE_PATH = ROOT_DIR / "params.yaml"