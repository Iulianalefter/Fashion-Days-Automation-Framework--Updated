from pages.base_page import Base_page
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class ForgotPasswordPage(Base_page):
    EMAIL_INPUT = (By.ID, "recover-password")
    RECOVERY_BUTTON =(By.ID, "recover-submit")
    EMAIL_ERROR_MESSAGE =(By.CLASS_NAME, "error-message")

    def navigate_to_forgot_password_page(self):
        self.driver.get("https://www.fashiondays.ro/customer/recover-password")

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def clean_email_text_field(self):
        self.driver.find_element(*self.EMAIL_INPUT).clear()

    def click_recover_button(self):
        self.driver.find_element(*self.RECOVERY_BUTTON).click()

    def verify_email_error_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.EMAIL_ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None" # nu s-a afisat elementul

        assert actual_message == expected_message, f'Error, the message is incorrect'





