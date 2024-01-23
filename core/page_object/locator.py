""" Classes-locators for different pages in MightyFields application. """

from selenium.webdriver.common.by import By


class SingInPageLocators():
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    SUBMIT_BUTTON = (By.ID, 'login')


class DashboardPageLocators():
    PROFILE_DROPDOWN = (By.ID, 'profile-dropdown')
    START_A_NEW_CASE_BUTTON = (By.ID,'addNewCase')


class StartANewCaseLocators():
    TITLE_CATEGORIES = (By.XPATH, "//span[text()='Categories']")
    CATEGORY_TEST = (By.ID, '60619c3cfdba81010065765c')
    SIMPLE_TEST_FORM = (By.ID, '60798817aaf9f9010022930b')


class CasePageLocators():
    CREATE_BUTTON = (By.CLASS_NAME, 'confirm')
    NAME_FIELD = (By.ID, 'febcae89-87f6-40f6-8672-725c17ee641b')
    AGE_FIELD =  (By.ID, '48bdbf37-2ddd-4075-84a9-9e12ab55a61d')
    COUNTRY_FIELD = (By.ID, 'e6c7be8e-c654-41a5-9183-9c11a30efb26') 
    LANGUAGE_HANDLER_RADIO_BUTTON = (By.CLASS_NAME, 'handle')
    LEVEL_ENGLISH_FIELD = (By.ID, '53526619-bcf2-4cfe-b30c-e69a648d0946')
    LEVEL_GERMAN_FIELD = (By.ID, '44911e88-03d5-43b5-8708-d342224c7168')
    FINISH_TAB = (By.CSS_SELECTOR, 'li[class="list-group-item ng-scope"]')
    CLOSE_CASE_BUTTON = (By.ID, 'close')
    YES_CLOSE_CASE_BUTTON = (By.CLASS_NAME, 'confirm')