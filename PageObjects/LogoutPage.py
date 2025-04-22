from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.profile_dropdown_xpath = "//p[@class='oxd-userdropdown-name']"
        self.logout_link_xpath = "//a[text()='Logout']"

    def logout(self):
        profile = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.profile_dropdown_xpath)))
        profile.click()

        logout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.logout_link_xpath)))
        logout_button.click()
