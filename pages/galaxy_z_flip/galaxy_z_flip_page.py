from base.my_selenium_driver import SeleniumDriver
import utilities.logger as log
import logging
import time

class galaxy_z_flip(SeleniumDriver):
    log = log.myLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    _cookie_button = "//button[@class ='cookie-bar__close cookie-bar__main-close']"
    galaxyflip_phone_name = "/html//div[@id='content']/div/div/div[3]/div/div[1]/section//div[@class='pd03-product-finder__content']/div[1]/div[2]//div[@class='pd03-product-card__product-name']/a[@href='/in/smartphones/galaxy-z-flip5/']/p[@class='pd03-product-card__product-name-text']"
    galaxyflip_phone_price = "/html//div[@id='content']/div/div/div[3]/div/div[1]/section//div[@class='pd03-product-finder__content']/div[1]/div[2]//div[@class='pd03-product-card__product-content-primary']/div[3]/p[2]"
    galaxyflip_buy_button = "/html//div[@id='content']/div/div/div[3]/div/div[1]/section//div[@class='pd03-product-finder__content']/div[1]/div[2]//div[@class='pd03-product-card__label-cta-wrap']/button[@href='javascript:;']"
    galaxyflip_exchange_no_thanks_button = "//div[@id='product__tradein_data']//ul[@role='list']/li[2]/a[@role='button']//div[@class='s-cta-text']"
    galaxyflip_assured_buyback_none_button = "//li[@id='assurednone']//label[@class='hubble-pd-radio__label js-assured-pop']//span[@class='s-label-inner']"
    galaxyflip_samsung_care_none_button = "//li[@id='carenone']//span[@class='s-label']/span[@class='s-label-inner']"
    galaxyflip_continue_button = "/html//div[@id='wrap']/div[@class='hubble-price-bar is-fixed is-minimized']//div[@class='hubble-price-bar__price-cta']/a[@role='button']"
    galaxyflip_continue_button_2 = "/html//div[@id='content__addon']/section[@class='hubble-addon-page']/div[4]//a[@title='your shopping cart']/span[@class='s-cta-text']"
    galaxyflip_paynow_button = "/html//div[@id='__next']/main[@class='site-content']/div[@class='container']/div[@class='content-container']/div[@class='content-body-holder']//button[.='Pay Now']"



    def closeCookieButton(self):
        self.elementClick(self._cookie_button)

    def getPhoneNameText(self):
        self.getText(self.galaxyflip_phone_name)

    def getPhonePriceText(self):
        self.getText(self.galaxyflip_phone_price)

    def clickBuyButton(self):
        self.elementClick(self.galaxyflip_buy_button)



    def galaxy_z_flip_browsing(self):
        self.closeCookieButton()
        self.getPhoneNameText()
        self.getPhonePriceText()
        self.clickBuyButton()