*** Settings ***
Variables   ../../../data/input.py
*** Variables ***
${size}   //div[text()='${select_size}' and @role='option']
${color}    //div[@option-label='${select_color}']
${add_to_cart}      //button[@title='Add to Cart']
${cart_logo}    //a[contains(@class,'showcart')]
${proceed_to_checkout}      //button[text()='Proceed to Checkout']