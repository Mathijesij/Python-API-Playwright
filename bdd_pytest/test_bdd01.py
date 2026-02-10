from pytest_bdd import scenario, scenarios, given, when, then
import pytest

featureFile = 'C:\\Users\\MathijesiJohnbritto\\PycharmProjects\\demo\\bdd_pytest\\myfeatures\\one.feature'

def pytest_configure():
    pytest.AMT = 0

@scenario(featureFile, 'Withdrawal of money')
def test_withdrawal():
    pass

@given('the account balance is 100')
def current_balance():
    pytest.ATM = 100

@when('the account holder withdraws 30')
def withdraw_amount():
    pytest.ATM = pytest.ATM - 30

@then('the account balance should be 70')
def final_balance():
    assert pytest.ATM == 70

@scenario(featureFile, 'Removal of items from set')
def test_removalOfItems():
    pass

@given('A set of 3 fruits', target_fixture='myset')
def current_balance():
    myset = {'apple','banana','cherry'}
    return myset

@when('We remove a fruit from the set')
def remove_fruit(myset):
    myset.pop()
    print(myset)

@then('the set will have 2 fruits')
def final_set(myset):
    assert len(myset) == 2

