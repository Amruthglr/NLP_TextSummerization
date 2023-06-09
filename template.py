import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'textsummerizer'

file_list = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    f'src/{project_name}/exception/__init__.py'
    'config/congig.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'requirements.txt',
    'setup.py',
    'research/trails.ipynb',
    'Dockerfile',
]

for filepath in file_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory{filedir} for {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"creating a empty file : {filepath}")

    else:
        logging.info(f"{filename} already exists")
