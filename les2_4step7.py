from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    element1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")) # по Айди price и его значению=$100
    button = browser.find_element_by_id("book") #ищем кнопку по айди боок
    button.click()
    x = browser.find_element_by_id('input_value').text #берем текст из тега
    y = calc(x) 
    input = browser.find_element_by_id("answer") #ищем элемент с айди Ансвер(это поле)
    browser.execute_script("return arguments[0].scrollIntoView(true);", input) 
    # через execute_скрипт написали Джава код для того чтобы проскроллить до поля Инпут, который определили выше
    input.send_keys(y)
    submit1 = browser.find_element_by_id("solve").click()

finally:
    time.sleep(4)
    browser.quit()