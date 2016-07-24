
Feature: Demo of displaying output 2 scenarios passed but 1 failed on console

Scenario: A test that will PASS (stdout demo)

    Given Open browser and go to home page
    When Click on "contact us"
    Then Should see '123/456' address

Scenario: A test with And(Given) that will PASS (stdout demo)

    Given Open browser
    And Go to home page
    When Click on "contact us"
    Then Should see '123/456' address

Scenario: A test that will FAIL by assert (stdout demo)

    Given Open browser
    And Go to home page
    When Click on "my account"
    Then Should see 'Preferences' text