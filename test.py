from selenium import webdriver

import time


try:
    browser = webdriver.Firefox()
    browser.get("https://tap.az/")
    
    input_value = browser.find_element_by_id("keywords")
    input_value.send_keys("velosiped")
    
    submit = browser.find_element_by_css_selector("button.header-btn_search")
    submit.click()

    items = browser.find_elements_by_css_selector("a.add_bookmark")
    for i in items:
        i.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла