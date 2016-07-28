
from behave import given, when, then

#----------------------------------------------------------------------------------------------------------------------#
@given('I find order id from database')
def find_orderid_from_db(context):

    print("Finding an order from the database....")
    context.order_id = '12481632'

    print("Found an orders. Order number: {}".format(context.order_id))

#----------------------------------------------------------------------------------------------------------------------#
@when('I issue a refund for that order id')
def issue_refund(context):

    print("Trying to issue a refund for order number: {}".format(context.order_id))
    context.refund_stat = refund_by_id(context.order_id)

@when('I issue a refund on the same order')
def issue_repeat_refund(context):

    print("Trying to issue refund on same order: {}".format(context.order_id))

#----------------------------------------------------------------------------------------------------------------------#
@then('process payment to user')
def payment_should_process(context):
	if context.refund_stat == True:
	    print("Payment successfully processed")
	    print("Payment is for refund of order number: {}".format(context.order_id))
	else:
		raise Exception("Unexpected Payment error.")

@then('refund process will fail')
def refund_fails(context):

    print("The refund for order {} fail.".format(context.order_id))

#--------------------------------------------
# operation functions

def refund_by_id(uid):
	print("Refund")
	return True
