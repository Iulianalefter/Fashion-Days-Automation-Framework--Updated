from telnetlib import EC
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from browser import Browser

# in aceasta pagina punem toate metodele care sunt utile in orice pagina si nu neaparat specifice unei pagini
class Base_page(Browser):
    LOGIN_BUTTON = (By.ID, "pizokel_customer_submit")
    ACCEPT_COOKIES_BTN = (By.ID, "accept-cookie-policy")

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()


    def check_the_current_url(self, url):
        actual = self.driver.current_url
        expected_url = url
        assert actual == expected_url, f"Url-ul este gresit"

    def click_if_present_by_selector(self, by, selector):
        elem_list = self.driver.find_elements(by, selector)
        if len(elem_list) == 1:
            self.wait_scroll_and_click_elem_by_selector(by, selector)

    def wait_scroll_and_click_elem_by_selector(self, by, selector):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((by, selector)))
        elem = self.driver.find_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.driver.execute_script("arguments[0].click();", elem)

    def hover_by_elem(self, elem):
        actions = ActionChains(self.driver).move_to_element(elem)
        actions.perform()
        sleep(1)

    def click_accept_cookies_btn(self):
        self.click_if_present_by_selector(*self.ACCEPT_COOKIES_BTN)