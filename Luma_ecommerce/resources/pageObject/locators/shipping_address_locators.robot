*** Settings ***
Variables   ../../../data/input.py
*** Variables ***
${saved_address_0}  //input[@name='street[0]']
${saved_address_1}  //input[@name='street[1]']
${saved_address_2}  //input[@name='street[2]']
${city}     //input[@name='city']
${state}    //select[@name='region_id']
${state_option}     //option[contains(text(),'${select_state}')]
${post_code}    //input[@name='postcode']
${telephone}    //input[@name='telephone']
${fixed}    //td[text()='Fixed']
${next_btn}     //button/span[text()='Next']
${display_address}      //div[@class='billing-address-details']
${place_order}  //button[@title='Place Order']
${thank_you_message}    //h1/span
${order_id}     //a/strong
${order_id_message}     (//div[@class='checkout-success']/p)[1]