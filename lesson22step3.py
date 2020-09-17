from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(a,b):
    return str(int(a)+int(b))

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/selects1.html")
    
    num1 = browser.find_element_by_id("num1")
    a = num1.text
    num2 = browser.find_element_by_id("num2")
    b = num2.text
    result = calc(a,b)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла