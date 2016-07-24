from behave import given, when, then


@given("Open browser and go to home page")
def at_home_page(context):
    open_browser(context)
    go_to_home_page(context)
    print("Now open browser and go to home page...")

@given("Open browser")
def open_browser(context):
    print("Open browser")

@given("Go to home page")
def go_to_home_page(context):
    print("Go to home page")


@when('Click on "contact us"')
def click_contact_us(context):
    print('Clicking on "contact us" button...')

@when('Click on "my account"')
def click_my_account(context):
    print("I am clicking on my account")


@then("Should see '123/456' address")
def verify_address(context):
    print("I see the correct address")

@then("Should see 'Preferences' text")
def see_prefernces(context):
    print("Should see preferences")
    assert 1 == 2, "one is not same as two" #try to fail