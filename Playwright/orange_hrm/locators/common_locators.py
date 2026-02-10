class CommonLocators:
    # in user profile
    user_profile = "div[class='oxd-topbar-header-userarea']"
    about = "a[text='About']"
    support = "a[text='Support']"
    change_password = "a[text='Change Password']"
    logout = "a[text='Logout']"

    # menu
    search_placeholder = "Search"
    admin_text = "Admin"
    pim_text = "PIM"
    leave_text = "Leave"
    time_text = "Time"
    recruitment_text = "Recruitment"
    my_info_text = "My Info"
    performance_text = "Performance"
    dashboard_text = "Dashboard"
    directory_text = "Directory"
    maintenance_text = "Maintenance"
    claim_text = "Claim"
    buzz_text = "Buzz"

    # button
    add_button = "Add"
    cancel_button = "Cancel"
    save_button = "Save"

    # Success msg
    success_msg_css = ".oxd-text--toast-title"

    # Left menu
    left_menu_css = ".oxd-main-menu-item--name"

    input_text_xpath = "//div[label[text()=$$]]/following-sibling::div//input"

    dropdown_xpath = "//div[label[text()=$$]]/following-sibling::div"

    no_record_found_message = "No Records Found"

    no_record_found_message_css = "#oxd-toaster_1"
