from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from locators import locators

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com")

wait = WebDriverWait(driver, 10, poll_frequency=0.5)

elements = driver.find_element(By.XPATH, locators["elements"])
driver.execute_script("arguments[0].scrollIntoView(true);", elements)
elements.click()

widgets = driver.find_element(By.XPATH, locators["widgets"])
driver.execute_script("arguments[0].scrollIntoView(true);", widgets)
widgets.click()

auto_complete = driver.find_element(By.XPATH, locators["auto_complete"])
driver.execute_script("arguments[0].scrollIntoView(true);", auto_complete)
auto_complete.click()

multi = driver.find_element(By.XPATH, locators["multi_input_div"])
driver.execute_script("arguments[0].scrollIntoView(true);", multi)
multi.click()

input_box = driver.find_element(By.XPATH, locators["multi_input_box"])
input_box.send_keys("e")

option = wait.until(EC.presence_of_element_located((By.XPATH, locators["option_red"])))
option.click()

input_box = driver.find_element(By.XPATH, locators["multi_input_box"])
input_box.send_keys("o")

option2 = wait.until(EC.presence_of_element_located((By.XPATH, locators["option_indigo"])))
option2.click()

single_dropdown = driver.find_element(By.XPATH, locators["single_dropdown"])
driver.execute_script("arguments[0].scrollIntoView(true);", single_dropdown)
single_dropdown.click()

input_single = driver.find_element(By.XPATH, locators["single_input_box"])
input_single.send_keys("g")

green_option = wait.until(EC.presence_of_element_located((By.XPATH, locators["option_green"])))
green_option.click()

driver.quit()
