from os.path import exists
from pathlib import Path

import yaml


def get_files(files: str, separator: str):
    file_list: list[str] = files.split(separator)

    pbix_list = [
        {
            'file_name': Path(file).name,
            'file_path': Path(file),
            'file_workspace': Path(file).parent.name,
            'file_binary': get_file_binary(file),
        }
        for file in file_list
        if is_pbix(file)
    ]

    return pbix_list


def is_pbix(file: str) -> bool:
    return file.lower().endswith('.pbix')


def get_file_binary(file_path: str) -> bytes:
    if not exists(file_path):
        return None

    with open(file_path, 'rb') as file:
        bin_file: bytes = file.read()
        return bin_file


def get_workspace_id(workspace_name: str, workflow_config: str):
    with open(workflow_config, 'r') as yml_file:
        config = yaml.safe_load(yml_file)
        return config[workspace_name]['workspace_id']
