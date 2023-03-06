import requests
from bs4 import BeautifulSoup
import json
import os
import re
from utils import write_json

page = requests.get("https://famouspeople.astro-seek.com/filter_date/?umrti=&asc=&narozeni_den=nezalezi&narozeni_mesic=nezalezi&narozeni_rok=&narozeni_stat=&pohlavi=&razeni=datum_vek_sestupne")
soup = BeautifulSoup(page.content, 'html.parser')

current_dir = os.path.abspath(os.curdir)
dir_path = os.path.abspath(os.path.join(current_dir, os.pardir))

def get_pagination_links():
    pg_links = []
    pages = soup.find_all('a', {'class': 'page-off'})
    for page in pages:
        pg_links.append(page['href'])
        
    write_json('page_links', pg_links)
    
def init():
    get_pagination_links()
    
init()