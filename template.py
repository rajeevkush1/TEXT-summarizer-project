import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.DEBUG , format='%(asctime)s - %(levelname)s - %(message)s')
project_name = "MyProject"
list_of_files = [
    ".github/workflows/.gitkeep",   # GitHub workflow file
    f"src/{project_name}/__init__.py",  # Source directory with __
    f"src/{project_name}/components/__init__.py",  
    f"src/{project_name}/utils/__init__.py",
    f"/src/{project_name}/config/__init__.py",
    f"src/{project_name}/logging//__init__.py",  # Main application file
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",  # Configuration file
    "params.yaml",  # Parameters file
    "app.py",  # Main application file
    "requirements.txt",  # Requirements file
    "README.md",  # README file
    "main.py",  # Main entry point
    "Dockerfile",  # Dockerfile
    "setup.py",  # Setup file
    "research/trail.ipynb",  # Research directory with __init__.py
    "test.py"
    ]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
        logging.info(f"Created empty file: {file_path}")