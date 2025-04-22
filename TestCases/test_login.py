import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from PageObjects.LeavePage import Leave
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
username = "Admin"
password = "admin123"

@pytest.mark.run(order=1)
def test_login_function():
    # Initialize the driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)

    # Perform login
    login_page = Login(driver)
    login_page.login(username, password)

    # Verify that the dashboard page is loaded
    assert login_page.is_dashboard_loaded() is True, "Dashboard page failed to load"

    driver.quit()