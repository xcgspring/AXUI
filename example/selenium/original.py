
import selenium.webdriver as webdriver

browser = webdriver.Chrome(executable_path = r"C:\Users\cxuanx\Downloads\chromedriver.exe")
browser.get(r"http://www.bing.com")

searchEdit = browser.find_element_by_id("sb_form_q")
goButton = browser.find_element_by_id("sb_form_go")

searchEdit.send_keys("AXUI")
goButton.click()