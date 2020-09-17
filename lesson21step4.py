from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/math.html")
    
    input_value = browser.find_element_by_id("input_value")
    x = input_value.text
    result = calc(x)
    
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(result))
    
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    
    radiobox = browser.find_element_by_id("robotsRule")
    radiobox.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла