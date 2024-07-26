from bs4 import BeautifulSoup
import requests
from db_insert import insert_lake


abc = list(map(chr, range(97, 123)))
for char in abc:
    letter_page = requests.get(f"https://wldb.ilec.or.jp/Search/Lakename/{char}")
    soup = BeautifulSoup(letter_page.text, "lxml")
    table = soup.find("table", class_ = "list")
    links = table.find_all("a")
    hrefs = [link.get("href") for link in links]
    for url in hrefs:
        lake_page = requests.get(url)
        lake = BeautifulSoup(lake_page.text, "lxml")

        lake_name = lake.find("h2")
        lake_name = lake_name.contents[0].strip()

        table = lake.find("table", class_ = "lake-detail")
        table_data = table.find_all("td")

        lake_country = table_data[0].get_text(strip=True)

        lake_surface_area = None
        if len(table_data) > 1 and table_data[1].get_text(strip=True):
            lake_surface_area = table_data[1].get_text(strip=True)[:-8]
            try:
                lake_surface_area = float(lake_surface_area)
            except ValueError:
                lake_surface_area = None

        lake_mean_depth = None
        if len(table_data) > 2 and table_data[2].get_text(strip=True):
            lake_mean_depth = table_data[2].get_text(strip=True)[:-6]
            try:
                lake_mean_depth = float(lake_mean_depth)
            except ValueError:
                lake_mean_depth = None

        lake_volume = None
        if len(table_data) > 3 and table_data[3].get_text(strip=True):
            lake_volume = table_data[3].get_text(strip=True)[:-8]
            try:
                lake_volume = float(lake_volume)
            except ValueError:
                lake_volume = None
        
        insert_lake(name = lake_name, riparian_nations= lake_country, surface_area= lake_surface_area, mean_depth= lake_mean_depth, volume= lake_volume)


