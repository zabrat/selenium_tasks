from selenium import webdriver

browser = webdriver.Firefox()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = document.getElementsByTagName("button")[0];
button.scrollIntoView(true);
button.click()
assert True