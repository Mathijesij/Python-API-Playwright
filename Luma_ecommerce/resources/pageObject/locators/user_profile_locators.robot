
*** Variables ***
${nav_to_dropdown}  (//li[@class='customer-welcome'])[1]
${my_account}   (//a[text()='My Account'])[1]
${my_order}     //a[text()='My Orders']
${view_order_td}   //tr[td[text()='dynamic_order_id'] and td[a/span[text()='View Order']]]//a[span[text()='View Order']]
${get_order_id}     //td[@class='col id']