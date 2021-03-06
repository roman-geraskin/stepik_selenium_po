from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-default[href]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_CONTENTS = (By.CSS_SELECTOR, ".basket-title")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_REGISTER = (By.CSS_SELECTOR,
                    "#register_form [name=registration_submit]")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    MESSAGE_BOOK_ADDED_BOOK_NAME = (By.CSS_SELECTOR,
                                    "#messages > div:nth-child(1) strong")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "#messages > .alert-info strong")
