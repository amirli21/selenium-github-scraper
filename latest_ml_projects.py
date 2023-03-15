from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd


driver_options = webdriver.ChromeOptions()
driver_options.add_argument(' --incognito')
driver_path = 'C:\\webdrivers\\chromedriver.exe'


def create_webdriver():
    return webdriver.Chrome(executable_path=driver_path, chrome_options=driver_options)


github_link = 'https://github.com/collections/'
collection_name = 'machine-learning'


browser = create_webdriver()
browser.get(github_link+collection_name)

projects = browser.find_elements(By.XPATH, "//h1[@class='h3 lh-condensed']")

project_list = {}
for proj in projects:
   proj_name = proj.text 
   proj_url = proj.find_elements(By.XPATH, "a")[0].get_attribute('href')
   project_list[proj_name] = proj_url

browser.quit()

project_df = pd.DataFrame.from_dict(project_list, orient = 'index')

project_df.to_csv('project_list.csv')
