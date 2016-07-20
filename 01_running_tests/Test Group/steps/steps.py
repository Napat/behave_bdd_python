
from behave import given, when, then
#import login
from login import login

@given("I am the main directory")
def in_main_dir(context):
    print("----->1")

@then("I should also be in the main directory")
def also_in_main_dir(context):
    print("----->2")

@given("I am in subdirectory of main directory")
def in_sub_dir(context):
    pass

@given("I am negative test in main steps")
def negative(context):
    pass