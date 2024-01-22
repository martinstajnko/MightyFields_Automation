from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver

from core import constants


class CreateTask():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def create_and_close_task(self):

        self.driver.get(constants.URL)

        sleep(1)





                
        
        

