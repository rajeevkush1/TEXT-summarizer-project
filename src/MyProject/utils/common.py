import os
from box.exceptions import BoxValueError, BoxKeyError
from MyProject.logging import logger
import yaml
from pathlib import Path    
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any



@ensure_annotations 
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.
    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object. 
    Raises:
        BoxValueError: If the YAML file is empty or has invalid content.    
        """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            # if content is None:
            #     raise BoxValueError("YAML file is empty or has invalid content.")
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    
    except BoxValueError as e:
        raise ValueError(f"Value error while reading YAML file: {e}")
    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories if they do not exist.

    Args:
        path_to_directories (list[Path]): A list of directory paths to create.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of the file at the given path in KB.

    Args:
        path (Path): The path to the file."""
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"