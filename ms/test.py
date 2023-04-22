from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

try:
    driver = webdriver.Remote(
        command_executor='http://chrome:4444/wd/hub',
        options=chrome_options
    )
    driver.get("http://www.baidu.com")
    print(driver.title)
    driver.quit()
except Exception as e:
    print("An error occurred: ", e)

