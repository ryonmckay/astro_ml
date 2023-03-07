import json
import os
import requests
from bs4 import BeautifulSoup
from utils import write_json

current_dir = os.path.abspath(os.curdir)
dir_path = dir_path = os.path.abspath(os.path.join(current_dir, os.pardir)) 
links_path = os.path.join(dir_path, f"data/page_links.json")

def load_data():
    urls = []
    with open(links_path, 'r') as file:
        urls = json.load(file)
    return urls

def get_people_per_page(url, idx):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    people_pages = soup.find_all('td', {'class': 'w260_p5'})
    people_links = []
    
    for td in people_pages:
        link = td.find('a')
        people_links.append(link['href'])

    write_json(f"people_page_{idx}", people_links)

def init():
    urls = load_data()
    
    for idx, url in enumerate(urls[275: ]):
        get_people_per_page(url, idx)

init()