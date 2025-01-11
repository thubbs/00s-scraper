import requests
from bs4 import BeautifulSoup 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

url = "https://hellorayo.co.uk/absolute-radio-00s/playlist/"

driver = webdriver.Chrome()
driver.get(url)  
driver.implicitly_wait(5)

# deal with cookies popup
driver.switch_to.frame('sp_message_iframe_1153020')
driver.find_element(By.XPATH, "//button[2]").click()
driver.switch_to.default_content()

for pageLoad in range(50): # How many times selenium will click 'View more'. Web page seems to become unresponsive at around 80. 24 hours = ~10 clicks based on timestamps.
    time.sleep(3) # Needed to make sure everything loads before trying to scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") # Scroll to bottom to make sure 'View more' button is loaded before trying to click
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/main/div[3]/button").click()

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

trackNamesDump = soup.find_all('p', class_='sc-1vr93bj-11 fJkXMD')
artistNamesDump = soup.find_all('p', class_='sc-1vr93bj-11 fExKgU')

trackNames = []
artistNames = []

for track in trackNamesDump:
    trackNames.append(track.get_text(strip=True))

for artist in artistNamesDump:
    artistNames.append(artist.get_text(strip=True))

merged_list = list(zip(artistNames, trackNames))
print(merged_list)
