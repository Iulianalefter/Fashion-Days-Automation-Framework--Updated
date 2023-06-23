from selenium import webdriver

class Browser:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.fashiondays.ro/customer/authentication")
    driver.implicitly_wait(3)

    def close(self):
        self.driver.quit()
