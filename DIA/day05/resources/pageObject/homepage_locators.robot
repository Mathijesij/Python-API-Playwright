*** Settings ***
Resource    ../../data/data.robot

*** Variables ***
${leave_from}    //input[@placeholder='Leaving From']
${ource}      //input[@placeholder='Search Source']
${enter_source}    //*[text()= '${source_city}']
${going_To}    //input[@placeholder='Going To']
${enter_destination}       //*[text()='${destination_city}']
${search}      //span[text()='Search']

${today}       //a[text()='Today']
${tomorrow}        //a[text()='Tomorrow']
${sort_by}     //span[text()='Sort by']
${onward_journey_date}     //input[@placeholder='Onward Journey Date']
${date}    //*[text()='${enter_date}']