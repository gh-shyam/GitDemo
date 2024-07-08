import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Specify browser: chrome, firefox, or edge"
    )


# @pytest.fixture(scope="class")
# def setup(request):
#     browser_name = request.config.getoption("browser_name")
#     if browser_name == "chrome":
#         driver = webdriver.Chrome(executable_path=r"C:\Users\shyam\Desktop\drivers\chromedriver-win64\chromedriver.exe")
#     elif browser_name == "firefox":
#         driver = webdriver.Chrome(executable_path=r"C:\Users\shyam\Desktop\drivers\geckodriver.exe")
#     elif browser_name == "edge":
#         driver = webdriver.Chrome(executable_path=r"C:\Users\shyam\Desktop\drivers\msedgedriver")
#
#         # To get the URL
#     driver.get("https://rahulshettyacademy.com/angularpractice/")
#     driver.maximize_window()
#     driver.implicitly_wait(2)
#     request.cls.driver = driver
#     yield
#     driver.close()
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="chrome", help="Specify browser: chrome, firefox, or edge"
#     )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    driver = None

    if browser_name == "chrome":
        service = ChromeService(executable_path=r"C:\Users\shyam\Desktop\drivers\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FirefoxService(executable_path=r"C:\Users\shyam\Desktop\drivers\geckodriver.exe")
        driver = webdriver.Firefox(service=service)
    elif browser_name == "edge":
        service = EdgeService(executable_path=r"C:\Users\shyam\Desktop\drivers\msedgedriver.exe")
        driver = webdriver.Edge(service=service)

    if driver:
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
        driver.implicitly_wait(2)
        request.cls.driver = driver

    yield driver

    if driver:
        driver.quit()




