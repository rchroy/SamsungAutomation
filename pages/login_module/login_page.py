from base.my_selenium_driver import SeleniumDriver
import utilities.logger as log
import logging

class login(SeleniumDriver):
    log = log.myLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    ## Locators
    _cookie_button = "//button[@class ='cookie-bar__close cookie-bar__main-close']"
    login_Button="/html//nav[@id='component-id']//div[@class='nv00-gnb__utility-wrap']/div[3]/a[@role='button']"
    sign_in_button="/html//nav[@id='component-id']//div[@class='nv00-gnb__utility-wrap']/div[3]/ul[@role='menu']/li[1]/a[@role='menuitem']"
    login_via_samsung="/html//button[@id='b2cSignIn']"
    email_enter_text_box="/html//input[@id='iptLgnPlnID']"
    email_sign_in_next_button="/html//button[@id='signInButton']"
    password_entry="/html//input[@id='iptLgnPlnPD']"
    password_sign_in_next_button="/html//button[@id='signInButton']"
    after_login_button="/html//nav[@id='component-id']//div[@class='nv00-gnb__utility-wrap']/div[4]/a[@role='button']/span[@class='account-icon js-gnb-afterlogin-no-image']"
    my_page_link="//div[@id='wrap']/footer[@class='footer']//div[@class='footer-column']/div[4]/div[@class='footer-category']/div[@class='footer-category__list-wrap']/ul[@role='list']/li[1]/a[@href='/in/mypage/']"
    name_text="/html//div[@id='content']/div//div[@class='myd12-profile-and-your-message']//p[@class='myd12-profile-and-your-message__profile-name sdf-profile-name']"
      
    
    def closeCookieButton(self):
        self.elementClick(self._cookie_button)

    def clickLoginButton(self):
        self.elementClick(self.login_Button)

    def clickSignInButton(self):
        self.elementClick(self.sign_in_button)

    def login_via_samsung_Button(self):
        self.elementClick(self.login_via_samsung)

    def email_enter_text_box_Text(self):
        self.sendEmail(self.email_enter_text_box)

    def email_sign_in_next_button_click(self):
        self.elementClick(self.email_sign_in_next_button)

    def password_entry_box(self):
        self.sendPassword(self.password_entry)

    def password_sign_in_next_button_Click(self):
        self.elementClick(self.password_sign_in_next_button)

    def after_login_button_Click(self):
        self.elementClick(self.after_login_button)

    def my_page_link_Click(self):
        self.elementClick(self.my_page_link)

    def name_text_GetText(self):
        self.getText(self.name_text)

    def loginSamsung(self):
        self.closeCookieButton()
        self.clickLoginButton()
        self.clickSignInButton()
        self.login_via_samsung_Button()
        self.email_enter_text_box_Text()
        self.email_sign_in_next_button_click()
        self.password_entry_box()
        self.password_sign_in_next_button_Click()
        self.after_login_button_Click()
        self.my_page_link_Click()
        self.name_text_GetText()
        
