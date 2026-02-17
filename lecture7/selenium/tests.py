import os
import pathlib
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Convert local file path to a file URI
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

class WebpageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up Chrome driver once for all tests with Codespaces-specific flags"""
        chrome_options = webdriver.ChromeOptions()
        
        # Essential flags for running in a cloud/container environment
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(5) # Give the page a moment to load

    @classmethod
    def tearDownClass(cls):
        """Close the browser after all tests are finished"""
        if hasattr(cls, 'driver'):
            cls.driver.quit()

    def test_title(self):
        self.driver.get(file_uri("counter.html"))
        self.driver.save_screenshot("after_title.png")
        self.assertEqual(self.driver.title, "Counter")

    def test_increase(self):
        self.driver.get(file_uri("counter.html"))
        increase = self.driver.find_element(By.ID, "increase")
        increase.click()
        self.driver.save_screenshot("after_increaseclick.png")
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "1")

    def test_decrease(self):
        self.driver.get(file_uri("counter.html"))
        decrease = self.driver.find_element(By.ID, "decrease")
        decrease.click()
        self.driver.save_screenshot("after_decreaseclick.png")
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "-1")

if __name__ == "__main__":
    unittest.main()