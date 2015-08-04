
import selenium.webdriver as webdriver

browser = webdriver.Firefox()
browser.get(r"http://www.bing.com")

searchEdit = browser.find_element_by_id("sb_form_q")
goButton = browser.find_element_by_id("sb_form_go")

searchEdit.send_keys("AXUI")
goButton.click()
