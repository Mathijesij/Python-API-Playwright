from automationProject.resources.pages.home_page import HomePage
from automationProject.resources.pages.signup_login_page import SignupLoginPage
from automationProject.resources.pages.account_creation_page import AccountCreationPage
from automationProject.resources.pages.product_page import ProductPage
from automationProject.resources.pages.cart_page import CartPage
from automationProject.resources.pages.checkout_page import CheckoutPage
from automationProject.resources.pages.payment_page import PaymentPage
from automationProject.data.details import user_details
from automationProject.resources.locators.locators import locator
from playwright.sync_api import expect

def test_registerUser(page):

    home = HomePage(page, locator, user_details)
    signup_page = SignupLoginPage(page, locator, user_details)
    account_page = AccountCreationPage(page, locator, user_details)
    product_page = ProductPage(page, locator)
    cart_page = CartPage(page, locator)
    checkout_page = CheckoutPage(page, locator)
    payment_page = PaymentPage(page, locator, user_details)

    # Home page
    home.goto_home()
    home.click_signup_login()

    # Signup
    signup_page.signup()

    # Fill account information
    account_page.fill_account_info()
    expect(account_page.verify_account_created()).to_contain_text(user_details["account_created"])
    account_page.click_continue()

    expect(home.displayed_user_visible()).to_be_visible()

    # Add product to cart
    home.click_women_category()
    product_page.click_saree()
    product_page.open_first_product()
    product_page.add_to_cart()
    product_page.view_cart()

    # Checkout
    cart_page.proceed_to_checkout()
    checkout_page.place_order()

    # Payment
    payment_page.fill_payment_details()
    expect(payment_page.verify_order_placed()).to_contain_text(user_details["order_placed"])

    # Delete account
    page.get_by_text(user_details["delete_acc"]).click()
    expect(page.locator(locator["page_head_text"])).to_contain_text(user_details["account_deleted"])
