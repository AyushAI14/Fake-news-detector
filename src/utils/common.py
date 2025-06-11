import yaml
import os
from pathlib import Path
from src.logging import logger
from box import box
from box.exceptions import BoxValueError


def read_yaml_file(filepath:str)->box:
    """
    This reads the yaml file and return in form of box
    """
    try:
        with open(filepath,'r') as yamlfile:
            content = yaml.safe_load(yamlfile)
            logger.debug("Safely loaded the yaml file")
            return box(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
    

def create_dir(file_dir:list):
    for filepath in file_dir:
        os.makedirs(filepath,exist_ok=True)
        logger.debug(f"Created the directry at : {filepath}")