import os
from box import Box as ConfigBox
from pathlib import Path
import yaml
from typing import Union
from MyProject.logging import logger

def read_yaml(path_to_yaml: Union[str, Path]) -> ConfigBox:
    """Read a YAML file and return a ConfigBox object.
    Args:
        path_to_yaml (Union[str, Path]): Path to the YAML file
    Returns:
        ConfigBox: ConfigBox object containing the YAML contents
    """
    try:
        path = Path(path_to_yaml)
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path} loaded successfully")
            return ConfigBox(content or {})
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise

def create_directories(paths: list[Union[str, Path]], verbose: bool = True) -> None:
    """Create directories if they don't exist"""
    for path in paths:
        path = Path(path)
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

def get_size(path: Union[str, Path]) -> str:
    """Get size in KB"""
    path = Path(path)
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"


    