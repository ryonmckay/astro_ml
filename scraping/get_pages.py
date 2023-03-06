import requests
from bs4 import BeautifulSoup
import json
import os
import re

page = requests.get("https://famouspeople.astro-seek.com/filter_date/?umrti=&asc=&narozeni_den=nezalezi&narozeni_mesic=nezalezi&narozeni_rok=&narozeni_stat=&pohlavi=&razeni=datum_vek_sestupne")
soup = BeautifulSoup(page.content, 'html.parser')
# Get the current directory
current_dir = os.path.abspath(os.curdir)

# Get the parent directory
dir_path = os.path.abspath(os.path.join(current_dir, os.pardir))

# Print the parent directory
print(dir_path)

def write_json(fn, arr): 
    json_path = os.path.join(dir_path, f"data/{fn}.json")
    json_content = json.dumps(arr)
    
    with open(json_path, 'w') as f:
        f.write(json_content)

def get_pagination_links():
    pg_links = []
    pages = soup.find_all('a', {'class': 'page-off'})
    for page in pages:
        pg_links.append(page['href'])
        
    write_json('page_links', pg_links)
    
def init():
    get_pagination_links()
    
init()