from selenium import webdriver

# 開啟瀏覽器視窗(Chrome)
# 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄
chrome_driver_path = "./chromedriver"
chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path)

chrome_driver.get("http://www.python.org")
search_bar = chrome_driver.find_element_by_name("q")
print(search_bar.get_attribute("placeholder"))
