from selenium import webdriver

# 開啟瀏覽器視窗(Chrome)
# 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄
chrome_driver_path = "./chromedriver"
chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path)

chrome_driver.get("http://www.python.org")
search_bar = chrome_driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

logo = chrome_driver.find_element_by_class_name("python-logo")
# print(logo)

# get element with Xpath
search_input = chrome_driver.find_element_by_xpath('//*[@id="container"]/li[8]/ul/li[2]/a')
# print(search_input.text)



# get upcoming event
event_times = chrome_driver.find_elements_by_css_selector(".event-widget time")
event_title = chrome_driver.find_elements_by_css_selector(".event-widget a")
event_dict = {}
for n in range(len(event_times)):
    event_dict[n] = {
        "time": event_times[n].text,
        "title": event_title[n].text,
    },

print(event_dict)