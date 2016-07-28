# Pass around data from step to step
# Second scenario will fail because context is not sharing between scenario.

Feature: Sharing data scenario level using context

    Scenario: Process refund by order id

        Given I find order id from database
        When I issue a refund for that order id
        Then process payment to user

    Scenario: Refund should AttributeError on a refunded item

        When I issue a refund on the same order
        Then refund process will fail