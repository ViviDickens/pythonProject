from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.netflix_home import NetflixHome
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()


def test_netflix_home(driver):
    properties = {
        "url": "https://www.netflix.com"
    }
    url = properties["url"]

    page = NetflixHome(driver)
    page.open(url)
    page.maximize_window()
    title = page.get_page_title()
    print("Título de la página:", title)

    assert "Netflix" in title, f"El título no contiene 'Netflix', el título es: {title}"
