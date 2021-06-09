import selenium
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains

driver = selenium.webdriver.Chrome()
driver.set_window_size(1920, 1080)
action = ActionChains(driver)
website_url = 'http://localhost:3000/'

def login(email, password):
    driver.get(website_url)
    driver.find_element_by_xpath('//*[@id="root"]/div/nav/div/div[2]/div/div/div/a[1]/button').click()
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath('//*[@id="root"]/section/div/form/div/div[3]/button').click()

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

def find_slider(email="", password=""):
    try:
        if driver.find_element_by_class_name('MuiSlider-rail').is_displayed():
            return True
        else:
            return False
    except:
        return False

def change_assignment():
    try:
        # '/assignments/' subpage
        driver.find_element_by_xpath('//*[@id="root"]/div/nav/div/div[1]/ul/a[2]/li').click()
        source = driver.find_element_by_xpath(' //*[@id="root"]/div/div[2]/div/div[2]/div[1]/div')
        assignments = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/div/div/button[1]')
        ActionChains(driver).move_to_element(source).click(assignments).perform()
        return True
    except:
        return False

def logout():
    try:
        driver.find_element_by_xpath('//*[@id="root"]/div/nav/div/div[2]/div/div/div/a/button').click()
    except selenium.common.exceptions.NoSuchElementException:
        pass


class websiteTestCase(unittest.TestCase):

    # test id: test.F-REQ-2.2
    def test_7(self):
        driver.get(website_url)
        slider = driver.find_element_by_class_name('MuiSlider-rail')
        width = slider.size['width']
        passed = True
        try:
            action.click_and_hold(slider).move_by_offset(-width / 2, 0).release().perform()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[1]/div[1]/div/div/a').click()
        except:
            passed = False
        self.assertEqual(passed, True)

    # test id: test.F-REQ-1.1
    def test_8(self):
        driver.get(website_url)
        self.assertEqual(find_slider(), True)
        logout()

    # test id: test.F-REQ-1.2
    def test_9(self):
        signup('eee@gmail.com', 'passwd')
        self.assertEqual(find_slider(), True)
        logout()

    # test id: test.F-REQ-1.3
    def test_10(self):
        signup('bbb@gmail.com', 'passwd')
        self.assertEqual(find_slider(), True)
        logout()

    # test id: test.F-REQ-3.1
    def test_11(self):
        driver.get(website_url)
        self.assertEqual(change_assignment(), False)
        logout()

    # test id: test.F-REQ-3.2
    def test_12(self):
        signup('ddd@gmail.com', 'passwd')
        time.sleep(1)
        self.assertEqual(change_assignment(), True)
        logout()

    # test id: test.F-REQ-3.3
    def test_13(self):
        signup('ccc@gmail.com', 'passwd')
        time.sleep(5)
        self.assertEqual(change_assignment(), True)
        logout()

    # test id: test.F-REQ-4.1
    def test_14(self):
        self.assertEqual(signup('aaa@gmail.com', 'passwd'), True)
        logout()

    # test id: test.F-REQ-4.2
    def test_15(self):
        signup('fff@gmail.com', 'passwd')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div/nav/div/div[2]/div/div/div/a/button')
        time.sleep(1)
        self.assertEqual(signup('fff@gmail.com', 'passwd1'), False)
        logout()


if __name__ == '__main__':
    unittest.main()
