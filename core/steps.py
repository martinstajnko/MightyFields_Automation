from selenium.webdriver.remote.webdriver import WebDriver

from core import constants
from core.page_object.page import CasePage, DashboardPage, SignInPage, StartANewCase
from core.dataclass import User 


class CreateTask():
    """ Create a new task in a case """

    def __init__(self, driver: WebDriver, category: str, user: User):
        self.driver = driver
        self.category = category
        self.user = user

    def create_and_close_task(self):
        """ Create a new task in a case and close it """

        self.driver.get(constants.URL)

        sign_in_page = SignInPage(self.driver)
        sign_in_page.wait_for_sing_in_page()
        sign_in_page.sign_in(constants.EMAIL, constants.PASSWORD)

        dashboard_page = DashboardPage(self.driver)
        dashboard_page.wait_for_dashboard_page()
        dashboard_page.click_start_a_new_case_button()

        start_a_new_case = StartANewCase(self.driver)
        start_a_new_case.wait_for_title_categories()
        start_a_new_case.select_wanted_category(self.category)
        start_a_new_case.click_simple_test_form()

        case_page = CasePage(self.driver)
        case_page.wait_for_case_page()
        case_page.create_a_task()
        case_page.wait_until_create_button_is_not_presen()
        case_page.fill_form(self.user)
        case_page.click_tab_finish()
        case_page.click_close_case_button()
        case_page.confirm_close_case()
    





                
        
        

