Feature: Check the home page functionality

  Background:
    Given home: I am on home page

  @test_home_page
    Scenario: Verify home page url
        Then home: Check the url to be "https://www.fashiondays.ro/"

  @home_page_return
    Scenario: Click logo button and return to home
        When home: I click Fashion Days logo
        Then home: Check the url to be "https://www.fashiondays.ro/"

  @cat_and_subcat

   Scenario Outline: Hovering over category and subcategory

      When home: I hover over "<category>"
      Then home: I hover over "<subcategory>"

    Examples:
      | category              | subcategory |
      | Imbracaminte          | Rochii      |
      | Incaltaminte          | Sandale  |
