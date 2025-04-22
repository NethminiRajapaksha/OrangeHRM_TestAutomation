from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Leave:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.leave_menu_xpath = "//span[text()='Leave']/parent::a"  # XPath for the 'Leave' menu

    def navigate_to_leave(self):
        # Wait until the 'Leave' menu is clickable and click it
        leave_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.leave_menu_xpath)))
        leave_menu.click()

    def verify_leave_page(self):
        #  Check if 'Leave' page is loaded
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Leave']")))
        print("✅ Successfully navigated to the Leave page.")
