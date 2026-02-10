import input

leave_from= "xpath://input[@placeholder='Leaving From']"
source  =   "xpath://input[@placeholder='Search Source']"
enter_source = f"xpath://*[text()= '{input.source_city}']"
going_To =    "xpath://input[@placeholder='Going To']"
enter_destination = f"xpath://*[text()='{input.destination_city}']"
search = "xpath://span[text()='Search']"
today = "xpath://a[text()='Today']"
tomorrow = "xpath://a[text()='Tomorrow']"
sort_by = "xpath://span[text()='Sort by']"
onward_journey_date = "xpath://input[@placeholder='Onward Journey Date']"
date = f"xpath://*[text()='{input.enter_date}']"
month = f'xpath://span[contains(.,{input.enter_month})]'