import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.shopItems().click()  # Click on shop button
        print("Update Command 1")
        print("Update Command 2")
        print("Update Command 3")

        checkoutPage = CheckoutPage(self.driver)
        products = checkoutPage.getCardTitles()  # Get all product cards

        for product in products:
            product_name_element = product.find_element(By.XPATH, "div/h4/a")
            product_name = product_name_element.text
            if product_name == 'Blackberry':  # Check if product is 'Blackberry'
                product.find_element(By.XPATH, "div/button").click()  # Click on its Add to Cart button
                break  # Exit loop after finding and clicking on Blackberry

        self.driver.find_element(By.XPATH, "(//a[@class='nav-link btn btn-primary'])").click()  # Click on checkout button

        self.driver.find_element(By.XPATH, "(//button[@class='btn btn-success'])").click()  # Click on checkout button on checkout page

        print(self.driver.title)

        self.driver.find_element(By.ID, "country").send_keys('India')  # Enter country name

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))  # Wait for country suggestion to appear
        self.driver.find_element(By.LINK_TEXT, "India").click()  # Select India from suggestions

        self.driver.find_element(By.XPATH, "(//label[@for='checkbox2'])[1]").click()  # Check terms and conditions checkbox

        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()  # Click on purchase button

        # Validate success message
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']"))).text
        print(success_message)
        assert 'Success! Thank you!' in success_message
        print("Update Command 1")
        print("Update Command 2")
        print("Update Command 3")
