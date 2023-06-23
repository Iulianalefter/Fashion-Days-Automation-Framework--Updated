Feature: Check the Login functionality

  Background:
    Given login: I am a user on the login page

  @login1
  Scenario: Enter wrong credentials and check the error
    When login: I fill in an email "email@mail.com"
    When login: I fill in a password "pass"
    When login: I click the login button
    Then login: It shown an error message "Adresa de email sau parola este incorecta. Te rugam sa introduci o alta combinatie."

  @login2
Scenario: Enter correct credentials and login on the page
    When login: I fill in an email "iuliana.lefter@yahoo.com"
    When login: I fill in a password "Test1234!"
    When login: I click the login button
    Then login: I verify login page url

@empty_login_test
  Scenario: Leave empty login fields
    When login: I click the login button
    Then login: I verify the empty credentials error message "Acest camp este obligatoriu."
