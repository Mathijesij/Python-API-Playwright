from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutoCompletePage:

    locators = {
        "elements": "//h5[text()='Elements']",
        "widgets": "//div[text()='Widgets']",
        "auto_complete": "//span[text()='Auto Complete']",
        "multi_input_div": "//div[contains(@class,'--is-multi css-1hwfws3')]",
        "multi_input_box": "//div[contains(@class,'--is-multi')]//input",
        "option_red": "//div[contains(text(),'Red')]",
        "option_indigo": "//div[contains(text(),'Indigo')]",
        "single_dropdown": "//div[contains(@class,'value-container css-1hwfws3')]",
        "single_input_box": "//div[contains(@class,'value-container css-1hwfws3')]//input",
        "option_green": "//div[contains(text(),'Green')]",
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=0.5)

    def scroll_click(self, xpath):
        el = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
        el.click()

    def type_text(self, xpath, text):
        inp = self.driver.find_element(By.XPATH, xpath)
        inp.send_keys(text)

    def select_option(self, xpath):
        el = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        el.click()
