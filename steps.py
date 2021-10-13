from behave import *
from selenium import webdriver
import selenium.webdriver.support.ui as sel
import time
from selenium.webdriver.common.action_chains import ActionChains
from pywinauto import Application

from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import selenium.common.exceptions as selexcept
import logging
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller



@given('launch chrome browser')
def openHomePage(context):
    context.driver = webdriver.Chrome("C:\\Users\\jakub_1hexmn9\\Downloads\\chromedriver_win32\\chromedriver.exe")
    # context.driver=webdriver.Chrome()



@then(u'open plutus login page')
def step_impl(context):
    context.driver.get("https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn/related")
    time.sleep(5)

    context.driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button").click()
    time.sleep(3)
    context.driver.maximize_window()
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[6]/div[2]/div/div").click()
    time.sleep(4)
    keyboard = Controller()
    keyboard.press(enter)
    keyboard.release(enter)
    # actions = ActionChains(context.driver)
    # actions.perform()
    # actions.send_keys(Keys.LEFT)
    # actions.perform()
    # time.sleep(1)
    # actions.send_keys(Keys.ENTER)

    time.sleep(6000)
