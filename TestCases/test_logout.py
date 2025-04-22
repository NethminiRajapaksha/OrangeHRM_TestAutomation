import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from PageObjects.LogoutPage import Logout

@pytest.mark.run(order=3)
def test_logout_function():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page = Login(driver)
    login_page.login("Admin", "admin123")

    logout_page = Logout(driver)
    logout_page.logout()

    assert "login" in driver.current_url.lower()  # Check if logout was successful
    driver.quit()
