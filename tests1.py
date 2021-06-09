import selenium
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains

driver = selenium.webdriver.Chrome()
driver.set_window_size(1920, 1080)
action = ActionChains(driver)
website_url = 'http://localhost:3000/'


def signup(email, password):
    try:
        driver.get(website_url)
        driver.find_element_by_xpath('//*[@id="root"]/div/nav/div/div[2]/div/div/div/a[2]/button').click()
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_xpath('//*[@id="root"]/section/div/form/div[4]/button').click()
        time.sleep(1)
        return True
    except:
        return False


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

    # test id: test.F-REQ-4.3
    def test_3(self):
        signup('ggg@gmail.com', '')
        time.sleep(1)
        passed = True
        try:
            driver.find_element_by_xpath('//*[@id="root"]/div/nav/div/div[2]/div/div/div/a/button').click()
        except selenium.common.exceptions.NoSuchElementException:
            passed = False
        self.assertEqual(passed, False)

    # test id: test.F-REQ-5.1
    def test_4(self):
        driver.get(website_url)
        time.sleep(1)
        passed = True
        try:
            driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[1]/div[1]/div/div/a').click()
        except:
            passed = False
        self.assertEqual(passed, True)

    # test id: test.F-REQ-5.2
    def test_5(self):
        driver.get(website_url)
        time.sleep(1)
        passed = True
        try:
            driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[1]/div[1]/a/div').click()
        except:
            passed = False
        self.assertEqual(passed, True)

    # test id: test.F-REQ-5.3
    def test_6(self):
        driver.get(website_url)
        signup('kkk@gmail.com', 'passwd')
        passed = True
        try:
            driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[1]/div[1]/a/div/img').click()
        except:
            passed = False
            self.assertEqual(passed, True)


if __name__ == '__main__':
    unittest.main()