
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from population_page import PopulationPage


def test_world_population():

    # Launch Chrome browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    population = PopulationPage(driver)

    population.open_website()

    population.print_population_count()

    driver.quit()