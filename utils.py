import os
import sys
import json

def search_path(name, starting_repo = sys.path[0]):
    for path, directories, files in os.walk(starting_repo):
        if name in files:
            return os.path.join(path, name)
            

def read_config():
    with open(search_path('config.json')) as json_file:
        config = json.load(json_file)
    return config
