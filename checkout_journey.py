import allure
from behave import *
from selenium.webdriver.common.by import By

@when('order one')
def add_item_one_for_removal(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button").click()


@when('order two')
def additemtwo(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button").click()


@when('order three')
def additemthree(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button").click()


@when('order four')
def additemfour(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/button").click()


@when('open cartbox')
def clickonCart(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click()

@when('remove one item and varify')
def removeoneitem(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button").click()

@when('click on checkout button')
def clickoncheckout(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[2]").click()

@when('enter firstname "{first}" and lastname "{last}" and zipcode "{zipp}"')
def enternameandzip(context,first,last,zipp):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input").send_keys(first)
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input").send_keys(last)
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input").send_keys(zipp)

@when('click on continue button')
def continuebutton(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/input").click()

@when('varify the total ammount')
def varifyammount(context):
  status=context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[8]").is_displayed()
  assert status is True
  screenshot = context.driver.get_screenshot_as_png()
  allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)

@when('click on finish button')
def finishbutton(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]").click()

@then('varify the final page')
def finalpage(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/h2").is_displayed()
    screenshot = context.driver.get_screenshot_as_png()
    allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)




