from Playwright.details import user_details
from Playwright.locators import locator
from playwright.sync_api import Page, expect

# Register User and place an order
def test_registerUser(page:Page):
    page.goto(user_details["url"])

    # navigate to signup or login page
    click_signup_or_login = page.get_by_text(user_details["signup_or_login"])
    click_signup_or_login.click()

    # fill details in signup
    enter_name = page.get_by_placeholder(user_details["name"])
    enter_name.fill(user_details["user_name"])

    enter_email = page.locator(locator['sign_up_email'])
    enter_email.fill(user_details["user_email"])

    click_signup_btn = page.get_by_role("button",name=user_details["signup_btn"])
    click_signup_btn.click()

    # enter your information page
    select_title = page.locator(locator["title"])
    select_title.set_checked(True)

    enter_password = page.get_by_label(user_details["label_password"])
    enter_password.fill(user_details["password"])

    select_day_dob = page.locator(locator["days"])
    select_day_dob.select_option(user_details["dob_day"])

    select_month_dob = page.locator(locator["months"])
    select_month_dob.select_option(user_details["dob_month"])

    select_year_dob = page.locator(locator["years"])
    select_year_dob.select_option(user_details["dob_year"])

    enter_first_name = page.get_by_label(user_details["label_firstname"])
    enter_first_name.fill(user_details["first_name"])

    enter_last_name = page.get_by_label(user_details["label_lastname"])
    enter_last_name.fill(user_details["last_name"])

    enter_address = page.locator(locator["address1"])
    enter_address.fill(user_details["address"])

    select_country = page.locator(locator["country"])
    select_country.select_option(user_details["country"])

    enter_state = page.get_by_label(user_details["label_state"])
    enter_state.fill(user_details["state"])

    enter_city = page.locator(locator["city"])
    enter_city.fill(user_details["city"])

    enter_zipcode = page.locator(locator["zipcode"])
    enter_zipcode.fill(user_details["zipcode"])

    enter_mobile_number = page.get_by_label(user_details["label_mobilenumber"])
    enter_mobile_number.fill(user_details["mobile_number"])

    click_create_acc_btn = page.get_by_role("button", name=user_details["create_acc_btn"])
    click_create_acc_btn.click()

    #successfully created
    verify_account_created = page.locator(locator["page_head_text"])
    expect(verify_account_created).to_contain_text(user_details["account_created"])

    click_continue_btn = page.get_by_text(user_details["continue_btn"])
    click_continue_btn.click()

    #user-name display in home page
    wait_for_user_name_visible = page.locator(locator["displayed_user_name"])
    expect(wait_for_user_name_visible).to_be_visible()

    # add a product in to cart
    click_women = page.locator(locator["women"])
    click_women.click()

    click_saree = page.locator(locator["saree"])
    click_saree.click()

    hover_to_first_saree = page.locator(locator["first_product"])
    hover_to_first_saree.click()

    click_add_to_cart = page.locator(locator["add_to_cart"])
    click_add_to_cart.click()

    # view the product
    click_view_cart = page.locator(locator["view_cart"])
    click_view_cart.click()

    click_proceed_to_checkout = page.locator(locator["proceed_to_checkout"])
    click_proceed_to_checkout.click()

    click_place_order = page.locator(locator["place_order"])
    click_place_order.click()

    # payment
    enter_name_on_card = page.locator(locator["name_on_card"])
    enter_name_on_card.fill(user_details["name_on_card"])

    enter_card_number = page.locator(locator["card_number"])
    enter_card_number.fill(user_details["card_number"])

    enter_cvc = page.locator(locator["cvc"])
    enter_cvc.fill(user_details["cvc"])

    enter_exp_month = page.locator(locator["expire_month"])
    enter_exp_month.fill(user_details["exp_month"])

    enter_exp_year = page.locator(locator["expire_year"])
    enter_exp_year.fill(user_details["exp_year"])

    click_pay_and_order_btn = page.get_by_role("button", name=user_details["pay_and_order_btn"])
    click_pay_and_order_btn.click()

    # after placed order
    verify_order_placed = page.locator(locator["page_head_text"])
    expect(verify_order_placed).to_contain_text(user_details["order_placed"])

    click_continue_btn.click()

    # account deleted
    click_delete_account = page.get_by_text(user_details["delete_acc"])
    click_delete_account.click()

    verify_account_deleted = page.locator(locator["page_head_text"])
    expect(verify_account_deleted).to_contain_text(user_details["account_deleted"])

    click_continue_btn.click()

    # visible of signup/login again after deleting account
    signup_or_login_visible = page.locator(locator["signup_login"])
    expect(signup_or_login_visible).to_be_visible()


