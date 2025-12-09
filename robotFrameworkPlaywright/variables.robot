*** Variables ***
${browser}  chromium
${url}  https://automationexercise.com/

${signup_or_login}  text='Signup / Login'

${name}     input[placeholder='Name']
${email}    input[data-qa='signup-email']
${signup_btn}   text='Signup'

${title}    text='Mr.'
${password}     input[id='password']
${dob_days}     select[id='days']
${dob_month}    select[id='months']
${dob_year}     select[id='years']
${first_name}   input[id='first_name']
${last_name}    input[id='last_name']
${address}      input[id='address1']
${country}      select[id='country']
${state}        input[id='state']
${city}         input[id='city']
${zipcode}      input[id='zipcode']
${mobile_number}    input[id='mobile_number']
${create_account_btn}   text='Create Account'
${continue_btn}     text='Continue'

${account_created_successfully}     text=Logged in as Steve

${delete_account}    text='Delete Account'