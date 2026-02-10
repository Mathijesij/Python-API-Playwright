*** Settings ***
Variables     ../../../data/input.py
*** Variables ***
${style}       //div[text()='${shopping_option}']
${hoodie}    //li/a[contains(text(),'${product_name}')]
${product_1}    (//li[@class='item product product-item'])[1]
