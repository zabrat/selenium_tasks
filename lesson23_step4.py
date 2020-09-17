import time
from selenium import webdriver
import math
import pyperclip

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Firefox()
	browser.get("http://suninjuly.github.io/alert_accept.html")

	but = browser.find_element_by_css_selector("button.btn-primary")
	but.click()

	alert = browser.switch_to.alert
	alert.accept()

	browser.get("http://suninjuly.github.io/alert_redirect.html?")
	input_value = browser.find_element_by_id("input_value").text
	result = calc(input_value)

	answer = browser.find_element_by_id("answer")
	answer.send_keys(str(result))

	submit = browser.find_element_by_css_selector("button.btn")
	submit.click()

	alert = browser.switch_to.alert
	alert_text = alert.text
	addToClipBoard = alert_text.split(': ')[-1]
	pyperclip.copy(addToClipBoard)
finally:
	time.sleep(30)
	browser.quit()

