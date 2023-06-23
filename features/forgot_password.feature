Feature: Check the Forgot password functionality
  # se ruleaza inainte de fiecare scenariu
  Background:
    Given login: I am a user on the login page
    When  login: I click on the forgot password link

  @invalid
  Scenario: Check validation error message when email is invalid format
    When forgot_pass: I fill in my email "my_email@"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Adresa de email este invalida."

  @empty_email
  Scenario: Check validation error message when email is empty
    When forgot_pass: I make sure the email input is cleared
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Acest camp este obligatoriu"

  @multiple_scenarios
  Scenario Outline: Check various email validation
    When forgot_pass: I fill in my email "<email>"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "<expected_error>"


  Examples:
    |email         |expected_error                  |
    |test          |Adresa de email este invalida.  |
    |test1         |Adresa de email este invalida.  |
    |test2         |Adresa de email este invalida.  |