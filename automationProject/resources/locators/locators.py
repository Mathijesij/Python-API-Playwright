locator = {
    # for sign up
    "sign_up_email" : "//input[@data-qa='signup-email']",
    "title" : "//input[@value='Mrs']",
    "days" : "//select[@id='days']",
    "months" : "//select[@id='months']",
    "years" : "//select[@id='years']",
    "address1" : "//input[@id='address1']",
    "country" : "//select[@id='country']",
    "city" : "//input[@id='city']",
    "zipcode" : "//input[@id='zipcode']",
    "page_head_text" : "//h2/b",
    "displayed_user_name" : "//a[normalize-space(text())='Logged in as']",
    "signup_login" : "//a[normalize-space(text())='Signup / Login']",

    # for login
    "login_email" : "//input[@data-qa='login-email']",
    "login_to_acc_text" : "//div[@class='login-form']/h2",

    # category
    "women" : "//a[contains(normalize-space(), 'Women')]",
    "saree" : "//a[contains(normalize-space(), 'Saree')]",

    # in product page
    "first_product" : "(//a[text()='View Product'])[1]",
    "product_amount" : "(//div[@class='overlay-content'])[1]/h2",
    "product_name" : "(//div[@class='overlay-content'])[1]/p",
    "add_to_cart" : "//button[normalize-space()='Add to cart']",
    "view_cart" : "//u[text()='View Cart']",
    "proceed_to_checkout" : "//a[text()='Proceed To Checkout']",

    # in cart page
    "product_name_in_cart" : "//h4/a",
    "product_amount_in_cart" : "//td[@class='cart_price']/p",

    # place order
    "place_order" : "//a[text()='Place Order']",

    # payment
    "name_on_card" : "//input[@name='name_on_card']",
    "card_number" : "//input[@name='card_number']",
    "cvc" : "//input[@name='cvc']",
    "expire_month" : "//input[@name='expiry_month']",
    "expire_year" : "//input[@name='expiry_year']"
}
