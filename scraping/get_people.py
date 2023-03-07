import json
import os
import requests
import re
from bs4 import BeautifulSoup
from utils import write_json, get_month_number

current_dir = os.path.abspath(os.curdir)
dir_path = dir_path = os.path.abspath(os.path.join(current_dir, os.pardir)) 
links_path = os.path.join(dir_path, f"data/people_page_1.json")

PLANETS_LIST = ['mercury', 'venus', 'mars', 'sun', 'moon', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
HOUSES_LIST = ['AC', '2', '3', 'IC', '5', '6', 'DC', '8', '9', 'MC', '11', '12']

def load_data():
    urls = []
    with open(links_path, 'r') as file:
        urls = json.load(file)
    return urls

def get_occupation(soup):
    strong = soup.find('strong', string='Occupation')
    occ = None
    
    if strong:
        div = strong.parent.find_next_sibling("div")
        occ = div.get_text().replace('\n', '')
        
    return occ
        

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

def get_house_details(soup, house):
    div = soup.find('a', string=house)
    h = {}
    
    if (div):
        div = div.parent
        next_divs = div.find_next_siblings('div', limit=2)
        
        for idx, d in enumerate(next_divs):
            if idx == 0:
                # its sign
                sign = d.find('img')
                if sign:
                    h["sign"] = sign.get('alt')
                else:
                    h["sign"] = None
                    
            if idx == 1:
                spans = d.find_all('span')
                
                h["pos_degrees"] = int(spans[0].get_text())
                h["pos_minutes"] = int(spans[1].get_text().replace('’', ''))
                    
    return h

def get_houses(soup):
    houses = {}
    
    for house in HOUSES_LIST:
        houses[f"house_{house}"] = get_house_details(soup, house)
    
    return houses

def get_gender(soup):
    div = soup.find('strong', string='Gender')
    g = None
    
    if (div):
        div = div.parent
        next_div = div.find_next_sibling("div")
        g = next_div.get_text().replace('\n', '')
        
    return g
        

def get_planet_details(soup, planet, birth_time):
    div = soup.find('span', string=planet.title())
    p = {}
    
    if (div):
        div = div.parent
        next_divs = div.find_next_siblings('div', limit=4)
        
        for idx, d in enumerate(next_divs):
            if idx == 0:
                # its sign
                sign = d.find_all('img')
                
                if sign:
                    img = sign[0]
                
                    if planet == 'moon'and birth_time is None:
                        img = sign[1]
                    p["sign"] = img.get('alt')
                else:
                    p["sign"] = None
                    
            if idx == 1:
                spans = d.find_all('span')
                
                p["pos_degrees"] = int(spans[0].get_text())
                p["pos_minutes"] = int(spans[1].get_text().replace('’', ''))
                
                if planet == 'moon'and birth_time is None:
                    p["pos_degrees"] = int(spans[2].get_text())
                    p["pos_minutes"] = int(spans[3].get_text().replace('’', ''))
                
            if idx == 2:
                p["house"] = d.get_text()
                if len(p["house"]) is 0:
                    p["house"] = None
                
                if planet == 'moon'and birth_time is None:
                    p["house"] = None
                
            if idx == 3:
                if d.get_text() == 'R':
                    p["retrograde"] = True
                    
    return p

def get_planets(soup, birth_time):
    planets = {}
    
    for planet in PLANETS_LIST:
        planets[planet] = get_planet_details(soup, planet, birth_time)
    
    return planets

def get_death(soup):
    div = soup.find('strong', string='Death')
    death = {"date": None, "cause": None}
    
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
    
    person["birth_day"] = int(day)
    person["birth_month"] = get_month_number(month)
    person["birth_year"] = int(year)
    person["birth_time"] = time
    
    # get planets and their props
    planets = get_planets(soup=soup, birth_time=time)
    for planet in planets.items():
        planet_name, planet_props = planet
        for prop in planet_props.items():
            prop_key, prop_val = prop
            person[f"{planet_name}_{prop_key}"] = prop_val
    
    # houses
    houses = get_houses(soup)
    for house in houses.items():
        house_name, house_props = house
        person[f"{house_name}_sign"] = None
        person[f"{house_name}_pos_degrees"] = None
        person[f"{house_name}_pos_minutes"] = None
        for prop in house_props.items():
            prop_key, prop_val = prop
            person[f"{house_name}_{prop_key}"] = prop_val
            
    # death date and cause
    death = get_death(soup)
    if death["cause"]:
        person["death_cause"] = death["cause"]
    else:
        person["death_cause"] = None
    
    if death["date"]:
        day, month, year = death["date"].split()
        person["death_day"] = int(day)
        person["death_month"] = get_month_number(month)
        person["death_year"] = int(year)
    else: 
        person["death_day"] = None
        person["death_month"] = None
        person["death_year"] = None
    
    person["occupation"] = get_occupation(soup)
    person["gender"] = get_gender(soup)
    
    return person

def init():
    # data = load_data()
    
    # people = []
    # for page in data[0:10]:
    #     person = get_personal_info(page)
    #     people.append(person)
        
    # write_json("people_sample", people)
    spinoza_url = "https://www.astro-seek.com/birth-chart/rachel-weisz-horoscope"
    spinoza = get_personal_info(spinoza_url)
    write_json("spinoza", spinoza)

init()
    
    