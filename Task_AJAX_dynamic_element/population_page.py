from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class PopulationPage:

    def __init__(self, driver):
        self.driver = driver

        self.url = "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"

        self.population_xpath = "//*[@class='counter-ticker is-size-2-mobile']"

    def open_website(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def print_population_count(self):
        wait = WebDriverWait(self.driver, 20)
        population_element = wait.until(EC.visibility_of_element_located((By.XPATH, self.population_xpath)))

        print("\nPrinting Live Population Count")
        print("Press CTRL + C to Stop\n")


        for i in range(5):

            population = population_element.text

            print("Current Population :", population)

            time.sleep(3)

