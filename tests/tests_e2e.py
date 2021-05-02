import selenium.webdriver
import pytest


ADMIN_USER = "test"
ADMIN_PASSWORD = "test"


@pytest.fixture
def driver():
    res = selenium.webdriver.Chrome()
    yield res
    res.quit()


def test_create_question():
    driver = selenium.webdriver.Chrome()

    driver.get("http://127.0.0.1:8000/polls/reset/")

    driver.get("http://127.0.0.1:8000/admin")
    element = driver.find_element_by_id("id_username")
    element.send_keys(ADMIN_USER)
    element = driver.find_element_by_id("id_password")
    element.send_keys(ADMIN_PASSWORD)
    element = driver.find_element_by_xpath('//input[@type="submit"]')
    element.click()

    breakpoint()
