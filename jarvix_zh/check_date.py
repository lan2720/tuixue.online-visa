"""

[无用]mac启动本地debug: /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
隐藏chromedriver的身份: https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver
"""
import random
import time
import os

import requests
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
          "Origin": "https://portal.ustraveldocs.com",
          "Referer": "https://portal.ustraveldocs.com/appointmentcancellation",
          "Content-Type": "application/x-www-form-urlencoded",
          "Accept-Language": "zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
          }
chrome_port = 9527
chrome_drive_path = "/Users/jarvixwang/.wdm/drivers/chromedriver/mac64/116.0.5845.187/chromedriver-mac-arm64/chromedriver"
# def check_date():
#     url = "https://portal.ustraveldocs.com/appointmentcancellation"

#     requests.post(url, )

from selenium import webdriver


# driver = webdriver.Chrome()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# service = Service()
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)
from selenium_stealth import stealth
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver import Remote
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options, ChromiumOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# options = Options()#webdriver.ChromeOptions()#ChromiumOptions()#Options()
# options.add_experimental_option("detach", True)
account_info = {"username": "wangjianan527@gmail.com",
                "password": "Zxc123qwe"}
elem_xpaths = {"username": '//input[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:username"]',
               "password": '//input[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:password"]',
               "login_button": '//input[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:loginButton"]',
               "cancel_tab": "//*[text()='Cancel Appointment']"}
user_data = "/Users/jarvixwang/Downloads/selenium/data"
os.makedirs(user_data, exist_ok=True)
class ReuseChrome(Remote):

    def __init__(self, command_executor, session_id):
        self.r_session_id = session_id
        Remote.__init__(self, command_executor=command_executor, desired_capabilities={})

    def start_session(self, capabilities, browser_profile=None):
        """
        重写start_session方法
        """
        if not isinstance(capabilities, dict):
            raise InvalidArgumentException("Capabilities must be a dictionary")
        if browser_profile:
            if "moz:firefoxOptions" in capabilities:
                capabilities["moz:firefoxOptions"]["profile"] = browser_profile.encoded
            else:
                capabilities.update({'firefox_profile': browser_profile.encoded})

        self.capabilities = options.Options().to_capabilities()
        self.session_id = self.r_session_id
        self.w3c = False

def bypass_test():
    # os.system(f"/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port={chrome_port}")
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument(f"--remote-debugging-port={chrome_port}")
    # chrome_options.add_argument(f"user-data-dir={user_data}")
    # chrome_options.add_argument("--headless")
    # chrome_options.headless = True
    chrome_options.add_argument("--user-data-dir=/Users/jarvixwang/Library/Application Support/Google/Chrome/Default")
    chrome_options.add_argument("start-maximized")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{chrome_port}")
    # chrome_options.add_argument("–-incognito")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 取消chrome受自动控制提示
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("detach", True)  # 不要自动关闭浏览器
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # 这里添加一些启动的参数
    # chrome_options.add_argument('--window-size=720,720')  # 设置浏览器窗口大小

    # chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')

    # try:
    # my_service =
    driver = webdriver.Chrome(service=ChromeService(executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),#service=ChromeService(chrome_drive_path),
                              options=chrome_options)
    print(f"加载driver")
    # except:
    #     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
    #                               options=chrome_options)


    # stealth(driver,
    #         languages=["en-US", "en"],
    #         vendor="Google Inc.",
    #         platform="Win32",
    #         webgl_vendor="Intel Inc.",
    #         renderer="Intel Iris OpenGL Engine",
    #         fix_hairline=True,
    #         )
    # driver.maximize_window()

    base_url = "https://portal.ustraveldocs.com"
    login_url = "https://portal.ustraveldocs.com/SiteLogin" # ?country=&language=
    # forget_password_url = "https://portal.ustraveldocs.com/ForgotPassword?country=&language="
    # check_date_url = "https://portal.ustraveldocs.com/appointmentcancellation"
    driver.get(base_url)#forget_password_url)
    driver.implicitly_wait(random.randint(3, 10) + random.random())
    time.sleep(random.randint(2, 10) + random.random())
    # executor_url = driver.command_executor._url
    # session_id = driver.session_id
    # print(f"executor_url: {executor_url}, session_id={session_id}")

    # return executor_url, session_id, chrome_options
    # return driver
    # time.sleep(5)
    # print("done")
    # try:
    #     myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:j_id131')))
    #     print("Login Page is ready!")
    # except TimeoutException:
    #     print("Loading took too much time!")

    # time.sleep(10)
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
    # #
    # driver.find_element(By.XPATH, elem_xpaths["username"])
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
    # driver.quit()
#
# def login(driver):#executor_url, session_id, chrome_options):
#     # driver = webdriver.Remote(command_executor=executor_url, options=chrome_options)
#     # driver.session_id = session_id
#     # print(f"新driver当前url", driver.current_url)
#
#     while driver.find_element(By.XPATH, elem_xpaths["username"]):
#         driver.find_element(By.XPATH, elem_xpaths["username"]).send_keys(account_info["username"])
#         driver.find_element(By.XPATH, elem_xpaths["password"]).send_keys(account_info["password"])
#         driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()

if __name__ == '__main__':
    # login()
    print("start")
    driver = bypass_test() # executor_url, session_id, chrome_options
    # print("验证码通过，返回到主页面")
    # time.sleep(10)
    # # executor_url = f"http://localhost:{chrome_port}"
    # # print(f"new_executor_url: {executor_url}")
    # # session_id = "5afd851b6f129c6a1c57155d0502ae91"
    # login(driver)#executor_url, session_id, chrome_options)