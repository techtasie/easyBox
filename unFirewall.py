import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.firefox.options import Options
class EasyBoxClient:
    def __init__(self, password):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        self.driver.get("http://easybox.local")
        sleep(2)
        self.page_has_loaded()
        self.driver.find_element_by_xpath('//*[@id="Password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="LoginBtn"]').click()
        sleep(2)
        self.page_has_loaded()
        self.driver.get("http://easybox.local/?net_firewall&mid=NetFirewall")
        sleep(5)
        self.page_has_loaded()
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div[6]/div[3]/div/div[1]/div[1]/input').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="resetR"]').click()
        sleep(15)
        self.page_has_loaded()
        lever = self.driver.find_element_by_xpath('//*[@id="fw_enable"]')
        ac = ActionChains(self.driver)
        ac.move_to_element(lever).click().perform()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="applyButton"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="continue"]').click()
        self.driver.quit() 


    def page_has_loaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'
    

def main():
    pwd = os.environ['login']
    client = EasyBoxClient(pwd)

if __name__ == "__main__":
    main()
