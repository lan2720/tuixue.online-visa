"""
issue: https://github.com/ultrafunkamsterdam/undetected-chromedriver/issues/1318
"""
import time
import undetected_chromedriver as webdriver
from selenium.webdriver.remote.webdriver import By
driver = webdriver.Chrome()#use_subprocess=True)
driver.get("https://www.baidu.com")
time.sleep(2)

driver.find_element(By.ID,
            "Registration:SiteTemplate:theForm:username"
        ).send_keys("sdsfhdfs")