import requests
from bs4 import BeautifulSoup



def find_pn(player_ID)->str:


    '''
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options


    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)

    find_name_url = f"https://sortitoutsi.net/search/database?search={player_ID}&type="
    browser.get(find_name_url)

    table = browser.find_element(By.CSS_SELECTOR,"table")
    table_split=table.text.split('\n')
    name_of_player=table_split[1]
    return name_of_player
    '''



    find_name_url = f"https://sortitoutsi.net/search/database?search={player_ID}&type="
    data = requests.get(find_name_url).text
    soup=BeautifulSoup(data, 'html.parser')
    table=soup.find('table')
    name=table.tbody.find("a")
    name=name.contents[0].rstrip("\n").strip()
    return name
