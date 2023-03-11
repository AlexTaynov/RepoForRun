import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://hlebrm.ru")

    def tearDown(self):
        self.driver.quit()

    def test_title(self):
        self.assertEqual(self.driver.title, "hlebrm")

    def test_catalog(self):
        link = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div/div/a')
        link.click()
        self.assertEqual(self.driver.current_url, "http://hlebrm.ru/catalog.html")

    def test_pills(self):
        pills = self.driver.find_element(By.XPATH, '//*[@id="pills-tab"]')
        self.assertIn('Торты', pills.text)
        self.assertIn('Хлеб', pills.text)
        self.assertIn('Пирожные', pills.text)
        self.assertIn('Выпечка', pills.text)

    def test_new_order(self):
        new_order = self.driver.find_element(By.XPATH, '//*[@id="navigation"]/li[5]/a')
        new_order.click()
        self.assertEqual(self.driver.current_url, "http://hlebrm.ru/new-order/")

        name = self.driver.find_element(By.XPATH, '//*[@id="form4Example1"]')
        name.click()
        name.clear()
        name.send_keys("Name")

        name = self.driver.find_element(By.XPATH, '//*[@id="form4Example2"]')
        name.click()
        name.clear()
        name.send_keys("Phone number")

        submit = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/form/button')
        submit.click()

        self.assertEqual(self.driver.current_url, 'http://hlebrm.ru/')


if __name__ == '__main__':
    unittest.main()
