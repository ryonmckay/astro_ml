import json
import os

current_dir = os.path.abspath(os.curdir)
dir_path = os.path.abspath(os.path.join(current_dir, os.pardir))

def write_json(fn, arr): 
    json_path = os.path.join(dir_path, f"data/{fn}.json")
    json_content = json.dumps(arr)
    
    with open(json_path, 'w') as f:
        f.write(json_content)