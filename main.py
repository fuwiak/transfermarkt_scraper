import pandas as pd
import numpy as np
# Importing options for the Opera module

from webdriver_manager.opera import OperaDriverManager

url = "https://www.transfermarkt.com/robert-lewandowski/profil/spieler/38253"

from selenium import webdriver


# https://github.com/operasoftware/operachromiumdriver/releases

# driver = webdriver.Opera()


driver = webdriver.Opera(OperaDriverManager().install())
playerPage = driver.get(url)
df = pd.read_html(driver.page_source)[0]

