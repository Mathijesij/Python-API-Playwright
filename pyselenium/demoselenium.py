# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# driver = webdriver.Chrome()
#
# driver.maximize_window()
# driver.get("https://demoqa.com")
#
# # Click on 'Elements'
# elements = driver.find_element(By.XPATH, "//h5[text()='Elements']")
# driver.execute_script("arguments[0].scrollIntoView(true);", elements)
# elements.click()
#
# # Click on 'Widgets'
# widgets = driver.find_element(By.XPATH, "//div[text()='Widgets']")
# driver.execute_script("arguments[0].scrollIntoView(true);", widgets)
# widgets.click()
#
# # Click on 'Auto Complete'
# auto_complete = driver.find_element(By.XPATH, "//span[text()='Auto Complete']")
# driver.execute_script("arguments[0].scrollIntoView(true);", auto_complete)
# auto_complete.click()
#
# time.sleep(3)
#
# # Multi-select input
# multi = driver.find_element(By.XPATH, "//div[contains(@class,'--is-multi css-1hwfws3')]")
# driver.execute_script("arguments[0].scrollIntoView(true);", multi)
# multi.click()
#
# input_box = driver.find_element(By.XPATH, "//div[contains(@class,'--is-multi')]//input")
# input_box.send_keys("e")
#
# wait = WebDriverWait(driver, 10, poll_frequency=0.5)
# option = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Red')]")))
# option.click()
# time.sleep(3)
#
# # Input second value
# input_box = driver.find_element(By.XPATH, "//div[contains(@class,'--is-multi')]//input")
# input_box.send_keys("o")
#
# option2 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Indigo')]")))
# option2.click()
# time.sleep(3)
#
# # Single-select input
# single_dropdown = driver.find_element(By.XPATH, "//div[contains(@class,'value-container css-1hwfws3')]")
# driver.execute_script("arguments[0].scrollIntoView(true);", single_dropdown)
# single_dropdown.click()
#
# input_single = driver.find_element(By.XPATH, "//div[contains(@class,'value-container css-1hwfws3')]//input")
# input_single.send_keys("g")
#
# green_option = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Green')]")))
# green_option.click()
# time.sleep(3)
#
# driver.quit()
