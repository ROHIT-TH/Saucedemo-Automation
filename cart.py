import allure
from behave import *
from selenium.webdriver.common.by import By

@when('add item one to cart')
def add_item_one_to_cart(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button").click()

@when('add item two')
def additemtwo(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button").click()


@when('add item three')
def additemthree(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button").click()


@when('add item four')
def additemfour(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/button").click()


@then('click on cart to verify')
def clickonCart(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click()
    screenshot = context.driver.get_screenshot_as_png()
    allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)