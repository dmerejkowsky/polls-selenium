import selenium.webdriver
import pytest

ADMIN_USER = "test"
ADMIN_PASSWORD = "test"


@pytest.fixture
def driver():
    res = selenium.webdriver.Chrome()
    yield res
    res.quit()


def test_create_question(driver):
    question = "Is it working ?"
    choice_1 = "yes"
    choice_2 = "no"

    driver.get("http://127.0.0.1:8000/polls/reset/")
    driver.get("http://127.0.0.1:8000/admin")
    element = driver.find_element_by_id("id_username")
    element.send_keys(ADMIN_USER)
    element = driver.find_element_by_id("id_password")
    element.send_keys(ADMIN_PASSWORD)
    element = driver.find_element_by_xpath('//input[@type="submit"]')
    element.click()

    driver.get("http://127.0.0.1:8000/admin/polls/question/add/")
    element = driver.find_element_by_id("id_question_text")
    element.send_keys(question)
    element = driver.find_element_by_id("id_choice_set-0-choice_text")
    element.send_keys(choice_1)
    element = driver.find_element_by_id("id_choice_set-1-choice_text")
    element.send_keys(choice_2)

    element = driver.find_element_by_xpath('//input[@value="Save"]')
    element.click()

    driver.get("http://127.0.0.1:8000/polls")
    element = driver.find_element_by_tag_name("a")
    element.click()
    element = driver.find_element_by_id("choice1")
    element.click()
    element = driver.find_element_by_xpath('//input[@value="Vote"]')
    element.click()

    page_source = driver.page_source
    assert question in page_source
    assert "yes -- 1 vote" in page_source
