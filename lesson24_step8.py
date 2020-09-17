from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    book = browser.find_element_by_id("book")
    buy = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book.click()

    input_value = browser.find_element_by_id("input_value")
    x = input_value.text
    result = calc(x)
    
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(result))

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
