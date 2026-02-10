from pytest_bdd import scenario, scenarios, given, when, then
from pytest_bdd import parsers
import pytest

featureFile = 'C:\\Users\\MathijesiJohnbritto\\PycharmProjects\\demo\\bdd_pytest\\myfeatures\\parameterize.feature'

scenarios(featureFile)

@given('there are 3 varieties of fruits', target_fixture='fruits')
def existing_fruits():
    fruits = {'apples','grapes','strawberrys'}
    return fruits

@when('we add a same variety of fruit')
def add_a_fruit(fruits):
    fruits.add('grapes')

@then('there is same count of varieties')
def same_count(fruits):
    assert len(fruits) == 3

@then ('if we add a different variety of fruit')
def add_diff_variety(fruits):
    fruits.add('cherry')

@then(parsers.parse('the count of varieties increases to {count:d}'))
def count_increases(fruits, count):
    print('\nFruits:',fruits)
    print('Count: ',count)
    assert len(fruits) == count

@given(parsers.parse('There are {count:d} fruits'), target_fixture='start_fruits')
def existing_fruits(count):
    print('\nFruits Count: ',count)
    return dict(count=count, eat=0)

@when(parsers.parse('I eat {eat:d} fruits'))
def eat_fruits(start_fruits, eat):
    start_fruits['eat'] += eat
    print('Eaten Fruits Count: ',start_fruits)

@then(parsers.parse('I should have {left:d} fruits'))
def should_have_left_fruits(start_fruits, left):
    assert start_fruits['count'] - start_fruits['eat'] == left
    print('Balance Fruits Count: ',left)
