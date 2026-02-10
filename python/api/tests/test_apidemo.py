import pytest
import requests

from resources.config import *
from resources.resources import *
from resources.status_code_and_msg import *


BASE_URL = get_api_base_url()

# 1. GET all product list
def test_get_all_product_list():
    endpoint = productlist
    response = requests.get(f"{BASE_URL}{endpoint}")

    json_data = response.json()

    response_code = json_data.get("responseCode")
    product = json_data.get("products")

    print(f"\nAPI Response Code: {response_code}")
    print(f"Products: {product}")

    assert response_code == status_ok, f"Expected responseCode {status_ok} but got {response_code}"

# 2. POST all products list
def test_post_all_product_list():
    endpoint = productlist
    response = requests.post(f"{BASE_URL}{endpoint}")

    json_data = response.json()

    response_code = json_data.get("responseCode")
    message = json_data.get("message")

    print(f"\nAPI Response Code: {response_code}")
    print(f'Message: {message}')

    assert response_code == status_method_not_allowed, f"Expected responseCode {status_method_not_allowed} but got {response_code}"
    assert message == method_not_allowed_msg, f'Message mismatch: {method_not_allowed_msg}'

# 3. GET all brand list
def test_get_all_brand_list():
    endpoint = brandlist
    response = requests.get(f'{BASE_URL}{endpoint}')

    json_data = response.json()

    response_code = json_data.get("responseCode")
    brands = json_data.get("brands")

    print(f'\nBrand List: {brands}')
    print(f'ResponseCode: {response_code}')

    assert response_code == status_ok, f'Expected responseCode {status_ok} but got {response_code}'

# 4 PUT all brands list
def test_put_all_brands_list():
    endpoint = brandlist
    response = requests.put(f'{BASE_URL}{endpoint}')

    json_data = response.json()

    response_code = json_data.get('responseCode')
    message = json_data.get('message')

    print(f'\nResponseCode: {response_code}')
    print(f'Message: {message}')

    assert response_code == status_method_not_allowed, f"Expected responseCode {status_method_not_allowed} but got {response_code}"
    assert message == method_not_allowed_msg, f'Message mismatch: {method_not_allowed_msg}'

# 5 POST to search product
def test_post_search_product():
    search_product = get_search_product()

    endpoint = searchproduct
    response = requests.post(f'{BASE_URL}{endpoint}', data=search_product)

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    json_data = response.json()

    response_code = json_data.get("responseCode")
    products = json_data.get("products")

    print(f'\nResponseCode: {response_code}')
    print(f'Products: {products}')

    assert response_code == status_ok, f'Expected responseCode {status_ok} but got {response_code}'

# 6 POST to search product without parameter
def test_post_search_product_noparams():
    endpoint = searchproduct
    response = requests.post(f'{BASE_URL}{endpoint}')

    json_data = response.json()

    response_code = json_data.get("responseCode")
    message = json_data.get("message")

    print(f'\nResponseCode: {response_code}')
    print(f'Message: {message}')

    assert response_code == status_bad_request, f"Expected responseCode {status_bad_request} but got {response_code}"
    assert message == bad_request_msg_for_search, f'Message mismatch: {bad_request_msg_for_search}'

# 7 POST to verify login with valid details
def test_verify_valid_login():
    valid = get_valid_login()

    endpoint = verifylogin
    response = requests.post(f"{BASE_URL}{endpoint}", data=valid)

    json_data = response.json()

    response_code = json_data.get("responseCode")
    message = json_data.get("message")

    print(f"\nAPI Response Code: {response_code}")
    print(f"Message: {message}")

    assert response_code == status_ok, f"Expected responseCode {status_ok} but got {response_code}"
    assert message == user_exist_msg, f'Message mismatch: {user_exist_msg}'

# 8 POST to verify login without mail parameter
def test_verify_login_without_email_param():
    credentials = get_password()

    endpoint = verifylogin
    response = requests.post(f"{BASE_URL}{endpoint}", data=credentials)

    json_data = response.json()

    response_code = json_data.get("responseCode")
    message = json_data.get("message")

    print(f"\nAPI Response Code: {response_code}")
    print(f"Message: {message}")

    assert response_code == status_bad_request, f"Expected responseCode {status_bad_request} but got {response_code}"
    assert message == bad_request_msg_for_login, f'Message mismatch: {bad_request_msg_for_login}'

# 9 DELETE verify login
def test_delete_verify_login():
    endpoint = verifylogin
    response = requests.delete(f'{BASE_URL}{endpoint}')

    json_data = response.json()

    response_code = json_data.get("responseCode")
    message = json_data.get("message")

    print(f"\nAPI Response Code: {response_code}")
    print(f"Message: {message}")

    assert response_code ==status_method_not_allowed, f"Expected responseCode {status_method_not_allowed} but got {response_code}"
    assert message == method_not_allowed_msg, f'Message mismatch: {method_not_allowed_msg}'

# 10. Verify Login with invalid details
def test_verify_invalid_login():
    credentials = get_credentials()

    endpoint = verifylogin
    response = requests.post(f"{BASE_URL}{endpoint}", data=credentials)

    json_data = response.json()

    response_code = json_data.get("responseCode")
    message = json_data.get("message")

    print(f"\nAPI Response Code: {response_code}")
    print(f"Message: {message}")

    assert response_code == status_not_found, f"Expected responseCode {status_not_found} but got {response_code}"
    assert message == user_not_found_msg, f'Message mismatch: {user_not_found_msg}'

# 11. POST Create/Register User account
def test_create_account():
    new_user_payload = get_new_user_payload()

    endpoint = createaccount
    response = requests.post(f"{BASE_URL}{endpoint}", data=new_user_payload)

    assert response.status_code != status_service_unavailable, f"Server returned {status_service_unavailable} AutomationExercise API is down"

    json_data = response.json()

    response_code = json_data.get("responseCode")
    message = json_data.get("message")

    print(f"\nAPI Response Code: {response_code}")
    print(f"Message: {message}")

    assert response_code == status_created, f"Expected responseCode {status_created} but got {response_code}"
    assert message == user_created_msg, f'Message mismatch: {user_created_msg}'

# 12 DELETE METHOD to delete user account
def test_delete_user_account():
    delete_acc = get_delete_user()

    endpoint = deleteAccount
    response = requests.delete(f"{BASE_URL}{endpoint}", data=delete_acc)

    json_data = response.json()

    response_code = json_data.get("responseCode")
    message = json_data.get("message")

    print(f"\nAPI Response Code: {response_code}")
    print(f"Message: {message}")

    assert response_code == status_ok, f"Expected responseCode {status_ok} but got {response_code}"
    assert message == user_account_deleted_msg, f'Message mismatch: {user_account_deleted_msg}'

# 13 PUT update user account
def test_update_user_account():
    update_user = get_update_user()

    endpoint = updateAccount
    response = requests.put(f'{BASE_URL}{endpoint}', data=update_user)

    json_data = response.json()

    response_code = json_data.get("responseCode")
    message = json_data.get("message")

    print(f"\nAPI Response Code: {response_code}")
    print(f"Message: {message}")

    assert response_code == status_ok, f"Expected responseCode {status_ok} but got {response_code}"
    assert message == user_updated_msg, f'Message mismatch: {user_updated_msg}'

# 14 GET user account detail by email
def test_get_user_by_email():
    user_email = get_user_by_email()

    endpoint = getUserDetailByEmail
    response = requests.get(f'{BASE_URL}{endpoint}', params=user_email)

    json_data = response.json()

    response_code = json_data.get('responseCode')
    user_details = json_data.get("user")

    print(f'\nResponse Code: {response_code}')
    print(f'User Details: {user_details}')

    assert response_code == status_ok, f"Expected responseCode {status_ok} but got {response_code}"

# pytest tests/test_apidemo.py --html=tests/reports/report.html --self-contained-html -v