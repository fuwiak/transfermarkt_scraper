import pandas as pd
import numpy as np

url = "https://www.transfermarkt.com/robert-lewandowski/profil/spieler/38253"

from selenium import webdriver

driver = webdriver.Chrome()

playerPage = driver.get(url)
df = pd.read_html(driver.page_source)[0]

