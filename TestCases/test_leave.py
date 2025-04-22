import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from PageObjects.LeavePage import Leave
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.run(order=2)
def test_leave_function():
    # Initialize the driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    # Perform login
    login_page = Login(driver)
    login_page.login("Admin", "admin123")

    # Wait until Dashboard appears
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )

    # Initialize LeavePage and navigate to Leave
    leave_page = Leave(driver)
    leave_page.navigate_to_leave()

    # Verify successful navigation to the Leave page
    leave_page.verify_leave_page()

    driver.quit()
