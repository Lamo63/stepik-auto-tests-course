from selenium import webdriver
 
link = "http://suninjuly.github.io/cats.html"
try:

    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_id("button")
finally:
    browser.quit()