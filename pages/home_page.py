

from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Base_page

class HomePage(Base_page):
    LOGO_IMG = (By.CLASS_NAME, 'hidden-xs.visible-sm.visible-md.visible-lg.logo-header-desktop')



    def navigate_to_home_page(self):
        sleep(5)
        self.driver.get('https://www.fashiondays.ro/')

    def click_logo_img(self):
        sleep(1)
        self.driver.find_element(*self.LOGO_IMG).click()

    def verify_page_url(self, expected_url):
        sleep(1)
        actual = self.driver.current_url
        assert actual == expected_url, f'URL este gresit. Expected: https://www.fashiondays.ro,actual{actual}'

    def hover_over_menu_category(self, category_name):
        sleep(1)
        elem = self.driver.find_element(By.XPATH, f'//span[normalize-space()="Imbracaminte"]')
        self.hover_by_elem(elem)

    def hover_over_menu_subcategory(self, subcategory_name):
        sleep(1)
        elem = self.driver.find_element(By.CLASS_NAME, "main-menu__item-child__title")
        self.hover_by_elem(elem)
