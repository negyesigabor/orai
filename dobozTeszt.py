from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")

def elementOne ():
    elementOne = driver.find_element(By.ID, value="element-one")
    elementOne.click()
    assert "blur" in elementOne.get_attribute("class")

def elementTwo (color):
    time.sleep(0.1)
    elementTwo = driver.find_element(By.ID, value="element-two")
    ActionChains(driver).move_to_element(elementTwo).perform()
    assert f"background-color: {color}" in elementTwo.get_attribute("style")

def elementThree ():
    time.sleep(5)
    elementThree = driver.find_element(By.ID, value="element-three")
    ActionChains(driver).double_click(elementThree).perform()
    #assert f"background-color: {color}" in elementTwo.get_attribute("style")

elementOne()
driver.save_screenshot("elementOneTest.png")
elementTwo("green")
driver.save_screenshot("elementTwoTest.png")
elementThree()
driver.save_screenshot("elementThreeTest.png")
print("Tesztek okésak")
driver.close()