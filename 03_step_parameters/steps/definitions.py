
from behave import given, then, when


@given('I have a new {item} in my cart')
def i_have_item_in_cart(context, item):

    print("Add item: {}".format(item))

@given('I brought "{qtty}" {item}')
def add_multiple_participants(context, item, qtty):

    print("The number of participants is: {}".format(qtty))

    print('--------------------')
    print ('Original {} quantity {} type {}'.format( item, qtty, type(qtty)))
    new_qtty = int(qtty)
    print ('Original {} quantity {} type {}'.format( item, new_qtty, type(new_qtty)))
    print('--------------------')

@when('I click on {btn}')
def click_button(context, btn):

    print("I am clicking the button: {}".format(btn))

@then('I should see "{txt_arg}"')
def i_should_see_text(context, txt_arg):

    txt = txt_arg.lower()
    if txt not in ['success', 'error']:
        raise Exception("Unexpected text passed in.")

    if txt == 'success':
        print("Item added!")
    else:
        print("Bad item!")
    print("Checking if I see the '{}' text".format(txt))
    print("PASS. I see the '{}' text".format(txt))
