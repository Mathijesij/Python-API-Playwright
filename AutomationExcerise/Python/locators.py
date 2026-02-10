# For use to checking the current page
current_page_highlight = "//a[@style='color: orange;' and normalize-space(text())='Home']"


# Click login / signup
login_signup = "//a[normalize-space(text())='Signup / Login']"
# New User
new_user_signup = "//h2[normalize-space(text())='New User Signup!']"
new_user_name = "//input[@name='name']"
new_user_email = "//input[@data-qa='signup-email']"
sign_up_button = "//button[@data-qa='signup-button']"
# Exists User
login_to_your_account = "//h2[text()='Login to your account']"
login_email = "//input[@data-qa='login-email']"
login_password = "//input[@data-qa='login-password']"
login_button = "//button[@data-qa='login-button']"
# after login
logged_in_as = "//a[normalize-space(text())='Logged in as']"

# Enter account information page
mrs = "//input[@value='Mrs']"
password = "//input[@id='password']"
select_day = "//select[@id='days']"
select_day_option = "//option[@value='19']"
select_month = "//select[@id='months']"
select_month_option = "//option[text()='August']"
select_year = "//select[@id='years']"
select_year_option = "//option[@value='2000']"
first_name = "//input[@id='first_name']"
last_name = "//input[@id='last_name']"
address_1 = "//input[@id='address1']"
select_country = "//select[@id='country']"
select_country_option = "//option[@value='India']"
state = "//input[@id='state']"
city = "//input[@id='city']"
zipcode = "//input[@id='zipcode']"
mobile_number = "//input[@id='mobile_number']"
create_account_button = "//button[@data-qa='create-account']"

account_created_text = "//h2/b[text()='Account Created!']"
continue_button = "//a[@data-qa='continue-button']"

delete_account = "//a[normalize-space(text())='Delete Account']"
delete_account_text = "//h2/b[text()='Account Deleted!']"

# Products
products = "//a[normalize-space(text())='Products']"
all_products = "//h2[normalize-space(text())='All Products']"
first_product = "(//a[normalize-space(text())='View Product'])[1]"

product_name = "//div[@class='product-information']/h2"
product_category = "//p[contains(text(),'Category')]"
product_rupees = "//span[contains(text(),'Rs.')]"
product_availability = "//b[contains(text(),'Availability')]"
product_condition = "//b[contains(text(),'Condition')]"
product_brand = "//b[contains(text(),'Brand')]"

add_to_cart = "//button[contains(@class,'cart')]"
continue_shopping = "//button[text()='Continue Shopping']"
view_cart = "//u[text()='View Cart']"

proceed_to_checkout = "//a[contains(@class,'check_out')]"
place_order = "//a[contains(text(),'Place Order')]"

#payment
name_on_card = "//input[@name='name_on_card']"
card_number = "//input[@name='card_number']"
cvc = "//input[@name='cvc']"
exp_month = "//input[@name='expiry_month']"
exp_year = "//input[@name='expiry_year']"
pay_and_confirm_order = "//button[@data-qa='pay-button']"

order_placed_text = "//b[text()='Order Placed!']"