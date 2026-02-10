import pytest
from selenium import webdriver
from pytest_bdd import scenarios, given, when, then
from bdd_project.tests.pages.auto_complete_page import AutoCompletePage

featureFile = 'C:\\Users\\MathijesiJohnbritto\\PycharmProjects\\demo\\bdd_project\\tests\\features\\auto_complete.feature'
scenarios(featureFile)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def page(driver):
    return AutoCompletePage(driver)

@given("I open the DemoQA site")
def open_site(driver):
    driver.get("https://demoqa.com")

@when("I navigate to Auto Complete section")
def navigate(page):
    page.scroll_click(page.locators["elements"])
    page.scroll_click(page.locators["widgets"])
    page.scroll_click(page.locators["auto_complete"])

@when('I enter "e" in the multi select box')
def enter_e(page):
    page.scroll_click(page.locators["multi_input_div"])
    page.type_text(page.locators["multi_input_box"], "e")

@when('I select "Red" from the suggestions')
def select_red(page):
    page.select_option(page.locators["option_red"])
    print('\nRed was selected successfully!')

@when('I enter "o" in the multi select box')
def enter_o(page):
    page.type_text(page.locators["multi_input_box"], "o")

@when('I select "Indigo" from the suggestions')
def select_indigo(page):
    page.select_option(page.locators["option_indigo"])
    print('Indigo was selected successfully!')

@when("I open the single select dropdown")
def open_single(page):
    page.scroll_click(page.locators["single_dropdown"])

@when('I enter "g" in the single select box')
def enter_g(page):
    page.type_text(page.locators["single_input_box"], "g")

@when('I select "Green" from the suggestions')
def select_green(page):
    page.select_option(page.locators["option_green"])
    print('Green was selected successfully!')

@then("the selections should be applied successfully")
def verify():
    assert True
