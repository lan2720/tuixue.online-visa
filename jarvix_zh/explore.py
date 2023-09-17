import random
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


account_info = {"username": "wangjianan527@gmail.com",
                "password": "Zxc123qwe"}
elem_xpaths = {"username": '//input[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:username"]',
               "password": '//input[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:password"]',
               "login_button": '//input[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:loginButton"]',
               "cancel_tab": "//*[text()='Cancel Appointment']"}



# 指定 Chrome 浏览器的可执行文件路径
chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# 创建 ChromeDriver 服务对象
service = webdriver.chrome.service.Service(executable_path=chrome_path)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=/Users/jarvixwang/Library/Application Support/Google/Chrome/Default")
chrome_options.add_argument('--incognito')  # 无痕窗口
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 隐藏自动化痕迹
# chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 隐藏输出的一堆乱七八糟的内容
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

# 创建 WebDriver 对象
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                          options=chrome_options)

# 打开网页
base_url = "https://portal.ustraveldocs.com"
driver.get(base_url)#'https://www.baidu.com/')
driver.execute_script(f"window.open('https://www.baidu.com', 'new window')")
driver.implicitly_wait(random.randint(3, 10) + random.random())
time.sleep(random.randint(5, 10) + random.random())
# #
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(random.randint(3, 10) + random.random())
time.sleep(random.randint(2, 10)+random.random())
driver.close()
time.sleep(random.randint(1, 10) + random.random())
driver.switch_to.window(driver.window_handles[0])
driver.implicitly_wait(random.randint(3, 10) + random.random())
time.sleep(random.randint(3, 10) + random.random())
driver.find_element(By.XPATH, elem_xpaths["username"]).send_keys(account_info["username"])
driver.implicitly_wait(random.randint(3, 10) + random.random())
time.sleep(random.randint(6, 10) + random.random())
driver.find_element(By.XPATH, elem_xpaths["password"]).send_keys(account_info["password"])
driver.implicitly_wait(random.randint(3, 10) + random.random())
time.sleep(random.randint(2, 10) + random.random())
driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()
driver.implicitly_wait(random.randint(3, 10) + random.random())
time.sleep(random.randint(1, 10) + random.random())
driver.find_element(By.XPATH, elem_xpaths["login_button"]).click()
driver.implicitly_wait(random.randint(3, 10) + random.random())
time.sleep(random.randint(4, 10) + random.random())
# cookie_list = driver.get_cookies()
# cookies = ";".join([item["name"] + "=" + item["value"] + "" for item in cookie_list])
driver.find_element(By.XPATH, elem_xpaths["cancel_tab"]).click()
time.sleep(random.randint(3, 10) + random.random())

# 关闭浏览器
driver.quit()

# Cloudflare Ray ID: 80833283bf0e1afb
# Cloudflare Ray ID: 808334641afea702