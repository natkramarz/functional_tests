import selenium
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains

driver = selenium.webdriver.Chrome()
driver.set_window_size(1920, 1080)
action = ActionChains(driver)
website_url = 'http://localhost:3000/'


class websiteTestCase(unittest.TestCase):

    # test id: test.F-REQ-2.3
    def test_1(self):
        driver.get(website_url)
        passed = True
        try:
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[1]/div[1]/div/div/a').click()
        except:
            passed = False
        self.assertEqual(passed, True)

    # test id: test.F-REQ-2.1
    def test_2(self):
        driver.get(website_url)
        slider = driver.find_element_by_class_name('MuiSlider-rail')
        width = slider.size['width']
        passed = True
        try:
            action.click_and_hold(slider).move_by_offset(width / 2, 0).release().perform()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[1]/div[1]/div/div/a').click()
        except:
            passed = False
        self.assertEqual(passed, True)

if __name__ == '__main__':
    unittest.main()