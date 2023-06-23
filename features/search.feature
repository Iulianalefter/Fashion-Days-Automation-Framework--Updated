Feature: Fashion Days Search feature

  Background:
    Given search: I am on home page

    @search
    Scenario Outline: Test search functionality
      When search: I search after "<query>"
      Then search: I click search button

      Examples:
      | query    |
      | papuci   |
      | fuste    |
      | rochie   |