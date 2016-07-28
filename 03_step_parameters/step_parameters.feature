# Example

Feature: Try passing parameters from feature to step file

Scenario: Passing step parameters

    Given I have a new 'iPad' in my cart
    And I have a new "Keyboard" in my cart
    When I click on "Next"
    And I click on "FINISH"
    Then I should see "Success"

Scenario: Add 10 participants in the call

    Given I brought "5" "lottery tickets"