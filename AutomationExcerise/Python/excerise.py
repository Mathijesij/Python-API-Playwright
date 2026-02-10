import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import locators

@pytest.mark.ex
def test_case_001(setup):
    driver = setup

    check_home_page_is_visible = driver.find_element(By.XPATH,locators.current_page_highlight)
    assert check_home_page_is_visible.is_displayed(), "Home page is not visible!"

    login_or_sign_up = driver.find_element(By.XPATH,locators.login_signup)
    driver.execute_script("arguments[0].scrollIntoView(true);", login_or_sign_up)
    login_or_sign_up.click()

    verify_new_signup_text = driver.find_element(By.XPATH,locators.new_user_signup)
    assert verify_new_signup_text.is_displayed(), "New User Signup! is not visible"

    enter_name= driver.find_element(By.XPATH,locators.new_user_name)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_name)
    enter_name.send_keys("Jessy")

    enter_email = driver.find_element(By.XPATH,locators.new_user_email)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_email)
    enter_email.send_keys("jessy2345@gmail.com")

    click_signup_btn = driver.find_element(By.XPATH,locators.sign_up_button)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_signup_btn)
    click_signup_btn.click()

    click_title = driver.find_element(By.XPATH,locators.mrs)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_title)
    click_title.click()

    enter_password = driver.find_element(By.XPATH,locators.password)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_password)
    enter_password.send_keys("jessy65458")

    select_dob_day = driver.find_element(By.XPATH,locators.select_day)
    driver.execute_script("arguments[0].scrollIntoView(true);", select_dob_day)
    select_dob_day.click()

    select_dob_day_option = driver.find_element(By.XPATH,locators.select_day_option)
    driver.execute_script("arguments[0].scrollIntoView(true);", select_dob_day_option)
    select_dob_day_option.click()

    select_dob_month = driver.find_element(By.XPATH,locators.select_month)
    driver.execute_script("arguments[0].scrollIntoView(true);", select_dob_month)
    select_dob_month.click()

    select_dob_month_option = driver.find_element(By.XPATH,locators.select_month_option)
    driver.execute_script("arguments[0].scrollIntoView(true);", select_dob_month_option)
    select_dob_month_option.click()

    select_dob_year = driver.find_element(By.XPATH,locators.select_year)
    driver.execute_script("arguments[0].scrollIntoView(true);", select_dob_year)
    select_dob_year.click()

    select_dob_year_option = driver.find_element(By.XPATH,locators.select_year_option)
    driver.execute_script("arguments[0].scrollIntoView(true);", select_dob_year_option)
    select_dob_year_option.click()

    enter_first_name = driver.find_element(By.XPATH,locators.first_name)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_first_name)
    enter_first_name.send_keys("Jessy")

    enter_last_name = driver.find_element(By.XPATH,locators.last_name)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_last_name)
    enter_last_name.send_keys("Jordan")

    enter_address = driver.find_element(By.XPATH,locators.address_1)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_address)
    enter_address.send_keys("F-270 George St N")

    select_country_info = driver.find_element(By.XPATH,locators.select_country)
    driver.execute_script("arguments[0].scrollIntoView(true);", select_country_info)
    select_country_info.click()

    select_country_info_option = driver.find_element(By.XPATH,locators.select_country_option)
    driver.execute_script("arguments[0].scrollIntoView(true);", select_country_info_option)
    select_country_info_option.click()

    enter_state = driver.find_element(By.XPATH,locators.state)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_state)
    enter_state.send_keys("ONTARIO")

    enter_city = driver.find_element(By.XPATH,locators.city)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_city)
    enter_city.send_keys("Peterborough")

    enter_zipcode = driver.find_element(By.XPATH,locators.zipcode)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_zipcode)
    enter_zipcode.send_keys("K9J 3H1")

    enter_mobile_number = driver.find_element(By.XPATH,locators.mobile_number)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_mobile_number)
    enter_mobile_number.send_keys("9058782725")

    click_create_account_btn = driver.find_element(By.XPATH,locators.create_account_button)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_create_account_btn)
    click_create_account_btn.click()

    ac_created_text = driver.find_element(By.XPATH,locators.account_created_text)
    assert ac_created_text.is_displayed(), "Account Created is not visible"

    click_continue_btn = driver.find_element(By.XPATH,locators.continue_button)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_continue_btn)
    click_continue_btn.click()

    click_delete_btn = driver.find_element(By.XPATH,locators.delete_account)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_delete_btn)
    click_delete_btn.click()

    ac_deleted_text = driver.find_element(By.XPATH,locators.delete_account_text)
    assert ac_deleted_text.is_displayed(), "Account Deleted is not visible"

def test_case_002(setup):
    driver = setup

    check_home_page_is_visible = driver.find_element(By.XPATH, locators.current_page_highlight)
    assert check_home_page_is_visible.is_displayed(), "Home page is not visible!"

    login_or_sign_up = driver.find_element(By.XPATH, locators.login_signup)
    driver.execute_script("arguments[0].scrollIntoView(true);", login_or_sign_up)
    login_or_sign_up.click()

    check_login_to_your_ac_visible = driver.find_element(By.XPATH, locators.login_to_your_account)
    assert check_login_to_your_ac_visible.is_displayed(), "Login to your account is not visible!"

    enter_login_email = driver.find_element(By.XPATH, locators.login_email)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_login_email)
    enter_login_email.send_keys("jessie24@gmail.com")

    enter_login_password = driver.find_element(By.XPATH, locators.login_password)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_login_password)
    enter_login_password.send_keys("Jessie@23456")

    click_login_btn = driver.find_element(By.XPATH, locators.login_button)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_login_btn)
    click_login_btn.click()

    after_logged_in = driver.find_element(By.XPATH, locators.logged_in_as)
    assert after_logged_in.is_displayed(), "User not successfully logged in!"

def test_case_003(setup):
    driver = setup

    check_home_page_is_visible = driver.find_element(By.XPATH, locators.current_page_highlight)
    assert check_home_page_is_visible.is_displayed(), "Home page is not visible!"

    click_product = driver.find_element(By.XPATH, locators.products)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_product)
    click_product.click()

    all_products_is_visible = driver.find_element(By.XPATH, locators.all_products)
    assert all_products_is_visible.is_displayed(), "All Products is not visible!"

    click_first_product = driver.find_element(By.XPATH, locators.first_product)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_first_product)
    click_first_product.click()

    check_product_name = driver.find_element(By.XPATH, locators.product_name)
    assert check_product_name.is_displayed(), "Product Name is not visible!"

    check_product_category = driver.find_element(By.XPATH, locators.product_category)
    assert check_product_category.is_displayed(), "Product Category is not visible!"

    check_product_rupees = driver.find_element(By.XPATH, locators.product_rupees)
    assert check_product_rupees.is_displayed(), "Product Rs is not visible!"

    check_product_availability = driver.find_element(By.XPATH, locators.product_availability)
    assert check_product_availability.is_displayed(), "Product Availability is not visible!"

    check_product_condition = driver.find_element(By.XPATH, locators.product_condition)
    assert check_product_condition.is_displayed(), "Product Condition is not visible!"

    check_product_brand = driver.find_element(By.XPATH, locators.product_brand)
    assert check_product_brand.is_displayed(), "Product Brand is not visible!"

def test_case_004(setup):
    driver = setup

    check_home_page_is_visible = driver.find_element(By.XPATH, locators.current_page_highlight)
    assert check_home_page_is_visible.is_displayed(), "Home page is not visible!"

    login_or_sign_up = driver.find_element(By.XPATH, locators.login_signup)
    driver.execute_script("arguments[0].scrollIntoView(true);", login_or_sign_up)
    login_or_sign_up.click()

    check_login_to_your_ac_visible = driver.find_element(By.XPATH, locators.login_to_your_account)
    assert check_login_to_your_ac_visible.is_displayed(), "Login to your account is not visible!"

    enter_login_email = driver.find_element(By.XPATH, locators.login_email)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_login_email)
    enter_login_email.send_keys("jessie24@gmail.com")

    enter_login_password = driver.find_element(By.XPATH, locators.login_password)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_login_password)
    enter_login_password.send_keys("Jessie@23456")

    click_login_btn = driver.find_element(By.XPATH, locators.login_button)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_login_btn)
    click_login_btn.click()

    after_logged_in = driver.find_element(By.XPATH, locators.logged_in_as)
    assert after_logged_in.is_displayed(), "User not successfully logged in!"

    click_product = driver.find_element(By.XPATH, locators.products)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_product)
    click_product.click()

    all_products_is_visible = driver.find_element(By.XPATH, locators.all_products)
    assert all_products_is_visible.is_displayed(), "All Products is not visible!"

    click_first_product = driver.find_element(By.XPATH, locators.first_product)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_first_product)
    click_first_product.click()

    click_add_to_cart = driver.find_element(By.XPATH, locators.add_to_cart)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_add_to_cart)
    click_add_to_cart.click()

    sleep(3)

    click_view_cart = driver.find_element(By.XPATH, locators.view_cart)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_view_cart)
    click_view_cart.click()

    click_proceed_to_checkout = driver.find_element(By.XPATH, locators.proceed_to_checkout)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_proceed_to_checkout)
    click_proceed_to_checkout.click()

    click_place_order = driver.find_element(By.XPATH, locators.place_order)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_place_order)
    click_place_order.click()

    enter_name_on_the_card = driver.find_element(By.XPATH, locators.name_on_card)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_name_on_the_card)
    enter_name_on_the_card.send_keys("Jessey")

    enter_card_number = driver.find_element(By.XPATH, locators.card_number)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_card_number)
    enter_card_number.send_keys("876543219761")

    enter_cvc = driver.find_element(By.XPATH, locators.cvc)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_cvc)
    enter_cvc.send_keys("764")

    enter_exp_month = driver.find_element(By.XPATH, locators.exp_month)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_exp_month)
    enter_exp_month.send_keys("11")

    enter_exp_year = driver.find_element(By.XPATH, locators.exp_year)
    driver.execute_script("arguments[0].scrollIntoView(true);", enter_exp_year)
    enter_exp_year.send_keys("2027")

    click_pay_and_confirm_order = driver.find_element(By.XPATH, locators.pay_and_confirm_order)
    driver.execute_script("arguments[0].scrollIntoView(true);", click_pay_and_confirm_order)
    click_pay_and_confirm_order.click()

    order_placed_message = driver.find_element(By.XPATH, locators.order_placed_text)
    assert order_placed_message.is_displayed(), "Ordered Placed is not visible!"






