Feature: Auto Complete widget on DemoQA

  Scenario: Select multiple and single values in Auto Complete widget
    Given I open the DemoQA site
    When I navigate to Auto Complete section
    And I enter "e" in the multi select box
    And I select "Red" from the suggestions
    And I enter "o" in the multi select box
    And I select "Indigo" from the suggestions
    And I open the single select dropdown
    And I enter "g" in the single select box
    And I select "Green" from the suggestions
    Then the selections should be applied successfully
