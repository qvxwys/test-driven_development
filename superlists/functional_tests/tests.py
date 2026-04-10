import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class NewVisitorTest(LiveServerTestCase):
    """Тест нового посетителя."""
    def setUp(self):
        """Initialize Chrome WebDriver."""
        self.browser = webdriver.Chrome()

    def check_for_row_in_list_table(self, row_text):
        """Подтверджение строки в таблице списка."""
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Test. Можно начать список и получить его позже."""

        self.browser.get(self.live_server_url)

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Купить павлиньи перья')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Купить павлиньи перья')

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Сделать мушку из павльиных перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # table = self.browser.find_element(By.ID, 'id_list_table')
        # rows = table.find_elements(By.TAG_NAME, 'tr')
        # self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])
        # self.assertIn(
        #     '2: Сделать мушку из павльиных перьев',
        #     [row.text for row in rows]
        #     )

        self.check_for_row_in_list_table('1: Купить павлиньи перья')
        self.check_for_row_in_list_table(
            '2: Сделать мушку из павльиных перьев'
            )

        self.fail('Закончить тест!')
