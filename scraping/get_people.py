import json
import os
import requests
import re
from bs4 import BeautifulSoup
from utils import write_json

current_dir = os.path.abspath(os.curdir)
dir_path = dir_path = os.path.abspath(os.path.join(current_dir, os.pardir)) 
links_path = os.path.join(dir_path, f"data/people_page_1.json")

PLANETS_LIST = ['mercury', 'venus', 'mars', 'sun', 'moon', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']

def load_data():
    urls = []
    with open(links_path, 'r') as file:
        urls = json.load(file)
    return urls

def get_birth_date_and_time(soup):
    tags = soup.find_all('div', {'class': 'fl'})
    day = ''
    month = ''
    year = ''
    time = None
    
    for idx, tag in enumerate(tags):
        strong = tag.find('strong', string='Date of Birth')
        
        if (strong):
            div = tags[idx+1]

            a_tags = div.find_all('a')
            date = a_tags[0].get_text()
        
            day = date.split()[0]
            month = date.split()[1]
            year = a_tags[1].get_text()
            
            strings = [string for string in div.strings if string.strip()]
            for string in strings:
                if ':' in string and '\n' in string:
                    time = string.replace('- ', '').replace('h', '').replace('\n', '')
                    
    return (day, month, year, time)

def get_name(soup):
    tag = soup.find('h2')
    tag = tag.extract()
    txt = tag.get_text(strip=True)
    new_txt = re.sub(r'\(.*?\)', '', txt)
    new_txt = new_txt.replace('- Birth Chart' ,'')
    return new_txt

def get_planet_details(soup, planet):
    div = soup.find('span', string=planet.title())
    p = {}
    
    if (div):
        div = div.parent
        next_divs = div.find_next_siblings('div', limit=4)
        
        for idx, d in enumerate(next_divs):
            if idx == 0:
                # its sign
                sign = d.find('img')
                if sign:
                    p["sign"] = sign.get('alt')
                else:
                    p["sign"] = None
                    
            if idx == 1:
                spans = d.find_all('span')
                
                p["pos_degrees"] = spans[0].get_text()
                p["pos_minutes"] = spans[1].get_text().replace('’', '')
                
            if idx == 2:
                p["house"] = d.get_text()
                
            if idx == 3:
                if d.get_text() == 'R':
                    p["retrograde"] = True
                    
    return p

def get_planets(soup):
    planets = {}
    
    for planet in PLANETS_LIST:
        planets[planet] = get_planet_details(soup, planet)
    
    return planets

def get_death(soup):
    div = soup.find('strong', string='Death')
    death = {}
    
    if (div):
        div = div.parent
        next_divs = div.find_next_siblings('div', limit=1)
        
        for idx, d in enumerate(next_divs):
            lnk = d.find('a')
            death["date"] = lnk.get_text()
            death["cause"] = d.find('span').find('a').get_text()

    return death

def get_personal_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    person = {}
    person["name"] = get_name(soup)

    day, month, year, time = get_birth_date_and_time(soup)
    
    person["birth_day"] = day
    person["birth_month"] = month
    person["birth_year"] = year
    person["birth_time"] = time
    
    planets = get_planets(soup)

    for planet in planets.items():
        planet_name, planet_props = planet
        for prop in planet_props.items():
            prop_key, prop_val = prop
            person[f"{planet_name}_{prop_key}"] = prop_val
        
    #     # for item in planet.items():
        #     key, val = item
        #     person[f"{planet}_{key}"] = val
    
    death = get_death(soup)
    person["death_cause"] = death["cause"]
    person["death_date"] = death["date"]
    
    return person

def init():
    # data = load_data()
    
    # people = []
    # for page in data[0:10]:
    #     person = get_personal_info(page)
    #     people.append(person)
        
    # write_json("people_sample", people)
    spinoza_url = "https://www.astro-seek.com/birth-chart/baruch-spinoza-horoscope"
    spinoza = get_personal_info(spinoza_url)
    print(spinoza)

init()
    
    