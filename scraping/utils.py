import json
import os

current_dir = os.path.abspath(os.curdir)
dir_path = os.path.abspath(os.path.join(current_dir, os.pardir))

def write_json(fn, arr): 
    json_path = os.path.join(dir_path, f"data/{fn}.json")
    json_content = json.dumps(arr)
    
    with open(json_path, 'w') as f:
        f.write(json_content)
        
def get_month_number(month_name):
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    return months.get(month_name.title())