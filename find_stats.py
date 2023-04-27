from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def process(player_name)->str:
    result_str=""
    for letter in player_name:
        if letter==" ":
            result_str+="-"
        else:
            result_str+=letter
    return unidecode(result_str.lower())

def find_s(player_ID, player_name)->list:
    player_name=process(player_name)
    find_stats_url=f"https://fminside.net/players/3-fm-23/{player_ID}-{player_name}"

    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    browser.get(find_stats_url)
    
    player_info={}
    table_pi=browser.find_element(By.ID, "player")
    info=table_pi.text
    info=info[info.find("PLAYER INFO")+11:info.find("CONTRACT")].strip()
    info=info.split("\n")
    for ind in range(0,len(info)-1,2):
        player_info[info[ind]]=info[ind+1]

    
    stats={}
    table_stats = browser.find_elements(By.CSS_SELECTOR,"tbody")
    for column in table_stats:
        column=column.text.split("\n")
        for element in column:
            l=len(element)
            stat_num=element[l-2:l].strip()
            stat_name=element[0:len(element)-2].strip()
            stats[stat_name]=int(stat_num)
    return [player_info,stats]

    