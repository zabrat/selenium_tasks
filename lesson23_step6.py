from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    but = browser.find_element_by_class_name("trollface")
    but.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(2)

    input_value = browser.find_element_by_id("input_value")
    x = input_value.text
    result = calc(x)
    
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(result))
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла