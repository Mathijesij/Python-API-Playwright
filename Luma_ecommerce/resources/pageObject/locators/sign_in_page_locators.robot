*** Variables ***
${sign_in}      (//a[contains(text(),'Sign In')])[1]
${valid_email}      id=email
${valid_pass}       id=pass
${sign_in_btn}      (//span[text()='Sign In'])[1]
${after_sign_in}    (//span[contains(text(),'Welcome')])[1]