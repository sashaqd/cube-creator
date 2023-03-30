from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import os
import time
page = 1

# Path to the folder where downloaded data sets will be saved
save_folder = '/Users/sasha/desktop/bayanat_data'
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

url = "https://admin.bayanat.ae/home/datasets?langKey=en"
driver = webdriver.Chrome()
driver.get(url)

wait = WebDriverWait(driver, 10)

# Find the first page link and click it to load the page
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".kt-pagination__link--active"))).click()

links = []
names = []
while True:
    # Scrape data from the current page
    div_element = driver.find_element(By.CSS_SELECTOR,"#datasetListing > div")
    div_children = div_element.find_elements(By.XPATH,"./*")

    for child in div_children:
        desired_child = child.find_element(By.XPATH,".//*[contains(@class, 'kt-widget4__username')][1]")
        print(desired_child.get_attribute("innerHTML"))
        names.append(desired_child.get_attribute("innerHTML"))
        link = desired_child.get_attribute("href")
        links.append(link)
        links.append("/")

    print(page)
    page += 1
    if page == 4:
        break

    try:
        #Find the next page link and click it to load the next page
        selector_path = "#page-selection > ul > li:nth-child(" + str(page + 3) + ")"
        element = driver.find_element(By.CSS_SELECTOR, selector_path)
        element.click()
        time.sleep(5)

    except:
        # No more pages to load
        break

curPath = '/Users/sasha/desktop/bayanat_data/'
nameCount = 0
for l in links:
    if l == "/":
        nameCount+=1
        continue
    driver.get(l)
    div_element = driver.find_element(By.CSS_SELECTOR,"#ResourceListing")
    div_children = div_element.find_elements(By.XPATH,"./*")
    for child in div_children:
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[contains(@class, 'btn btn-label-primary btn-bold btn-sm btn-icon-h kt-margin-l-10 download-btn-rsrc')][1]")))

            desired_child = child.find_element(By.XPATH,".//*[contains(@class, 'btn btn-label-primary btn-bold btn-sm btn-icon-h kt-margin-l-10 download-btn-rsrc')][1]")
            download_link = desired_child.get_attribute("href")
            print(names[nameCount])
            print(download_link)
            PATH = curPath + names[nameCount]

            if not os.path.exists(PATH):
                os.makedirs(PATH)

            options = Options()
            prefs = {"download.default_directory" : PATH}
            options.add_experimental_option("prefs",prefs)
            driver = webdriver.Chrome(options=options)
            driver.get(download_link)
            time.sleep(2)

        except:
            print("Element not found within timeout period")
driver.quit()

