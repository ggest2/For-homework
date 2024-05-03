from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
url = "https://www.naver.com/"
driver.get(url)
searchBox = driver.find_element(By.XPATH,'//*[@id="query"]')
searchBox.send_keys("식당")
time.sleep(1)
searchBox.send_keys(Keys.RETURN)
map = driver.find_element(By.XPATH,'//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a').click()
driver.switch_to.window(driver.window_handles[-1])
time.sleep(1)
iFrame = driver.find_element(By.ID,'searchIframe')
driver.switch_to.frame(iFrame)
restaurantGroup = driver.find_element(By.XPATH,'//*[@id="_pcmap_list_scroll_container"]')

last_height = driver.execute_script("return arguments[0].scrollTop;", restaurantGroup)
while True:
    driver.execute_script("arguments[0].scrollBy(0, 1000)", restaurantGroup)
    new_height = driver.execute_script("return arguments[0].scrollTop;", restaurantGroup)
    if new_height == last_height:
        break
    last_height = new_height
restaurant = []
i = 1
while True:
    try: 
        restaurantName = driver.find_element(By.XPATH,'//*[@id="_pcmap_list_scroll_container"]/ul/li[%d]/div[1]/a/div/div/span[1]'%i).text
        restaurantType = driver.find_element(By.CSS_SELECTOR,"#_pcmap_list_scroll_container > ul > li:nth-child(%d) > div.CHC5F > a > div > div > span.KCMnt"%i).text
        restaurant.append([restaurantName,restaurantType])
        i+=1
    except:
        break
print(restaurant)
    

