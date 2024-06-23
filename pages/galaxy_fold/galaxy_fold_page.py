from base.my_selenium_driver import SeleniumDriver
import utilities.logger as log
import logging
import time
import traceback
from selenium.webdriver.common.by import By
from traceback import print_stack
import utilities.logger as log
import logging
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class galaxy_fold(SeleniumDriver):
    log = log.myLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _cookie_button = "//button[@class ='cookie-bar__close cookie-bar__main-close']"
    galaxyfold_phone_price = "//div[@id='content']//div[@class='pd03-product-finder__wrap']//div[@class='pd03-product-finder__content']//div[4]//div[@class='pd03-product-card__product-content-primary']/div[3]/p[2]"
    galaxyfold_buy_button = "//div[@id='content']//div[1]/section/div[@class='pd03-product-finder__wrap']//div[@class='pd03-product-finder__content']//div[4]//div[@class='pd03-product-card__label-cta-wrap']/button[@href='javascript:;']"
    galaxyfold_exchange_no_thanks_button = "//div[@id='product__tradein_data']//ul[@role='list']/li[2]/a[@role='button']//div[@class='s-cta-text']"
    galaxyfold_assured_buyback_none_button = "/html//li[@id='assurednone']//label[@class='hubble-pd-radio__label js-assured-pop']//span[@class='s-option-name']"
    galaxyfold_samsung_care_none_button = "/html//li[@id='carenone']//span[@class='s-label']//span[@class='s-option-name']"
    galaxyfold_continue_button = "/html//div[@id='wrap']/div[@class='hubble-price-bar is-fixed is-minimized']//div[@class='hubble-price-bar__price-cta']/a[@role='button']"
    galaxyfold_continue_button_2 = "/html//div[@id='content__addon']/section[@class='hubble-addon-page']/div[4]//a[@title='your shopping cart']/span[@class='s-cta-text']"
    galaxyfold_paynow_button = "/html//div[@id='__next']/main[@class='site-content']/div[@class='container']/div[@class='content-container']/div[@class='content-body-holder']//button[.='Pay Now']"



    def closeCookieButton(self):
        self.elementClick(self._cookie_button)

    def getPhonePriceText(self):
        self.getText(self.galaxyfold_phone_price)

    def clickBuyButton(self):
        self.elementClick(self.galaxyfold_buy_button)


    def galaxy_fold_browsing(self):
        self.closeCookieButton()
        self.getPhonePriceText()
        self.clickBuyButton()
