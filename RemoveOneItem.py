import allure
from behave import *
from selenium.webdriver.common.by import By

@when('add item one for removal')
def add_item_one_for_removal(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button").click()


@when('add item two for removal')
def additemtwo(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button").click()


@when('add item three for removal')
def additemthree(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button").click()


@when('add item four for removal')
def additemfour(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/button").click()


@when('open cart')
def clickonCart(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click()


@then('remove one item and varify')
def removeoneitem(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button").click()
    screenshot = context.driver.get_screenshot_as_png()
    allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
