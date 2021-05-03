import selenium.webdriver
import pytest

ADMIN_USER = "test"
ADMIN_PASSWORD = "test"


class ResetPage:
    def __init__(self, driver):
        self.driver = driver

    def reset_db(self):
        self.driver.get("http://127.0.0.1:8000/polls/reset/")


class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://127.0.0.1:8000/admin")

    def login(self, user, password):
        element = self.driver.find_element_by_id("id_username")
        element.send_keys(user)
        element = self.driver.find_element_by_id("id_password")
        element.send_keys(password)
        element = self.driver.find_element_by_xpath('//input[@type="submit"]')
        element.click()

    def add_question(self, question, choices):
        self.driver.get("http://127.0.0.1:8000/admin/polls/question/add/")
        element = self.driver.find_element_by_id("id_question_text")
        element.send_keys(question)

        for i, choice in enumerate(choices):
            element = self.driver.find_element_by_id(f"id_choice_set-{i}-choice_text")
            element.send_keys(choice)

        element = self.driver.find_element_by_xpath('//input[@value="Save"]')
        element.click()


class VotePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://127.0.0.1:8000/polls")

    def vote_first_choice_on_first_question(self):
        element = self.driver.find_element_by_tag_name("a")
        element.click()
        element = self.driver.find_element_by_id("choice1")
        element.click()
        element = self.driver.find_element_by_xpath('//input[@value="Vote"]')
        element.click()


@pytest.fixture
def driver():
    res = selenium.webdriver.Chrome()
    yield res
    res.quit()


def test_create_question(driver):
    reset_page = ResetPage(driver)
    reset_page.reset_db()

    admin_page = AdminPage(driver)
    admin_page.login(ADMIN_USER, ADMIN_PASSWORD)
    admin_page.add_question("Is it working?", ["yes", "no"])

    vote_page = VotePage(driver)
    vote_page.vote_first_choice_on_first_question()

    page_source = driver.page_source
    assert "Is it working?" in page_source
    assert "yes -- 1 vote" in page_source
