Feature: Check the register functionality

  Background:
    Given register: I am a user on the register page

  @register_successfull
Scenario: Enter correct credentials and create a new account
    When register: I fill in an user "iulianalefter@yahoo.com"
    When register: I fill in a passwords "123Test."
    When register: I click on accept terms
    When register: I click the register_button
    Then home: Check the url to be "https://www.fashiondays.ro"

  @client_already_registered

  Scenario: Try to register with the credentials of an created account
    When register: I fill in an user "iuliana.lefter@yahoo.com"
    When register: I fill in a passwords "Test1234!"
    When register: I click on accept terms
    When register: I click the register_button
    Then register: I verify the already created account error message"UN CONT INREGISTRAT CU ACEASTA ADRESA DE E-MAIL EXISTA DEJA."