import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)


@given('launch chrome browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome(options=options)


@when('open Saucedemo homepage')
def SaucedemoOpen(context):
    context.driver.get("https://www.saucedemo.com/")


@when('enter username "{user}" and password "{pwd}"')
def Username_Password(context, user, pwd):
    context.driver.find_element(By.ID, "user-name").send_keys(user)
    context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input").send_keys(pwd)


@when('click on login button')
def clickonLogin(context):
    context.driver.find_element(By.ID, "login-button").click()


@then('user should be successful login')
def Successful(context):
    text = context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/div").text
    assert text == "Swag Labs"
    screenshot = context.driver.get_screenshot_as_png()
    # Attach the screenshot to the Allure report
    allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)


