""" Classes with methods for different pages in MightyFields application. """

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from core.dataclass import User
from core.enums import Countries, LanguageLevels 
from core.page_object.locator import CasePageLocators, DashboardPageLocators, SingInPageLocators, StartANewCaseLocators


class Basepage():
    """ Basepage class. """

    def __init__(self, driver):
        self.driver = driver

    def clean_field(self, field: tuple) -> None:
        """
        Clean the field.

        Args:
            field (tuple): Selector of the field and its locator.
        """        
        self.driver.find_element(*field).clear()

class SignInPage(Basepage):

    def wait_for_sing_in_page(self) -> None:
        """
        Wait for the sign in page to be visible.
        """
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((SingInPageLocators.EMAIL_FIELD)))
    
    def sign_in(self, email: str, password: str) -> None:
        """
        Sign in with the given email and password.

        Args:
            email (str): Email address. 
            password (str): Password for the email.
        """
        self._enter_email(email)
        self._enter_password(password)
        self.click_button_submit()

    def _enter_email(self, email: str) -> None:   
        self.clean_field(SingInPageLocators.EMAIL_FIELD)
        self.driver.find_element(*SingInPageLocators.EMAIL_FIELD).send_keys(email)

    def _enter_password(self, password: str) -> None:
        self.clean_field(SingInPageLocators.PASSWORD_FIELD)
        self.driver.find_element(*SingInPageLocators.PASSWORD_FIELD).send_keys(password)

    def click_button_submit(self) -> None:
        self.driver.find_element(*SingInPageLocators.SUBMIT_BUTTON).click()

class DashboardPage(Basepage):
    
    def wait_for_dashboard_page(self) -> None:
        """

        """

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((DashboardPageLocators.PROFILE_DROPDOWN)))


    def click_start_a_new_case_button(self) -> None:
        """
        """
        
        self.driver.find_element(*DashboardPageLocators.START_A_NEW_CASE_BUTTON).click()


class StartANewCase(Basepage):
    
    def wait_for_title_categories(self) -> None:
        """
        Wait for the title categories to be visible.
        """
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((StartANewCaseLocators.TITLE_CATEGORIES)))

    def select_wanted_category(self, wanted_category: str) -> None:
        """
        Select the wanted category.

        Args:
            category (str): Category to be selected.
        """
        categories = {
            'test': StartANewCaseLocators.CATEGORY_TEST,
        }

        category_locator = categories[wanted_category]
        self.driver.find_element(*category_locator).click()
        
        
    def click_simple_test_form(self) -> None:
        """ Click on the simple test form. """
        self.driver.find_element(*StartANewCaseLocators.SIMPLE_TEST_FORM).click()
        
    
class CasePage(Basepage):
    
    def wait_for_case_page(self) -> None:
        """ Wait for the case page to be visible. """
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((CasePageLocators.CREATE_BUTTON)))

    def create_a_task(self) -> None:
        """ Click on the create button. """
        self.driver.find_element(*CasePageLocators.CREATE_BUTTON).click()

    def wait_until_create_button_is_not_presen(self) -> None:
        """ Wait until the create button is not present. """
        WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((CasePageLocators.CREATE_BUTTON)))
    

    def fill_form(self, user: User) -> None:
        """
        Fill the form with the given user.

        Args:
            user (User): Dataclass, which defines the user.
        """
        self._enter_name(user.name)
        self._enter_age(user.age)
        self._select_country(user.country)

        language_handlers: list = self.driver.find_elements(*CasePageLocators.LANGUAGE_HANDLER_RADIO_BUTTON)        
        self._enable_language(user.language_1, user.language_1_level, language_handlers, 0)
        self._enable_language(user.language_2, user.language_2_level, language_handlers, 1)

    def click_tab_finish(self) -> None:
        """ Click on the finish tab. """
        self.driver.find_element(*CasePageLocators.FINISH_TAB).click()

    def click_close_case_button(self) -> None:
        """ Click on the close case button. """
        self.driver.find_element(*CasePageLocators.CLOSE_CASE_BUTTON).click()

    def confirm_close_case(self) -> None:
        """ Confirm the close case. """
        self.driver.find_element(*CasePageLocators.YES_CLOSE_CASE_BUTTON).click()

    def _enter_name(self, name: str) -> None:
        self.driver.find_element(*CasePageLocators.NAME_FIELD).send_keys(name)

    def _enter_age(self, age: int) -> None:
        age = str(age)
        self.driver.find_element(*CasePageLocators.AGE_FIELD).send_keys(age)

    def _select_country(self, country: Countries) -> None:        
        select = Select(self.driver.find_element(*CasePageLocators.COUNTRY_FIELD))
        select.select_by_visible_text(country.value)

    def _enable_language(self, language: bool, level: LanguageLevels, language_handlers: list, number: int) -> None:        
        if language:
            language_handlers[number].click()

            if number == 0:
                select = Select(self.driver.find_element(*CasePageLocators.LEVEL_ENGLISH_FIELD))
                select.select_by_visible_text(level.value)
            elif number == 1:
                select = Select(self.driver.find_element(*CasePageLocators.LEVEL_GERMAN_FIELD))
                select.select_by_visible_text(level.value)
            else:
                raise Exception("Wrong number of language handler")




