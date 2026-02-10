*** Variables ***
${url}      https://magento.softwaretestingboard.com
${browser}  chrome

#Sign In
${sign_in}      (//a[contains(text(),'Sign In')])[1]
${valid_email}      id=email
${valid_pass}       id=pass
${sign_in_btn}      (//span[text()='Sign In'])[1]

# error message
${get_error1}       //div[@for='email']
${get_error2}       //div[@for='pass']
${error_msg}        This is a required field.

#for gobal variable
${women}        //a/span[text()='Women']
${cloth}        (//li[@class='item'])[3]
${search}       //input[@id='search']
${cloth_name}       Hoodies & Sweatshirts for Women
${search_cloth}     //span[contains(text(),'${cloth_name}')]
${page_title}       //h1[@class='page-title']