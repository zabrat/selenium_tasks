import time
from selenium import webdriver
import os

try:
	browser = webdriver.Firefox()
	browser.get("http://suninjuly.github.io/file_input.html")

	firstname = browser.find_element_by_name("firstname")
	firstname.send_keys("a")

	firstname = browser.find_element_by_name("lastname")
	firstname.send_keys("a")

	firstname = browser.find_element_by_name("email")
	firstname.send_keys("a")

	file = browser.find_element_by_id("file")
	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, 'tips.txt')           # добавляем к этому пути имя файла 
	file.send_keys(file_path)

	submit = browser.find_element_by_css_selector("button.btn")
	submit.click()
finally:
	time.sleep(30)
	browser.quit()

