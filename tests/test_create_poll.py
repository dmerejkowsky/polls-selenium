import selenium.webdriver


def test_create_question():
    driver = selenium.webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/admin")
    breakpoint()
