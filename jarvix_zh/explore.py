from selenium import webdriver

# 指定 Chrome 浏览器的可执行文件路径
chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# 创建 ChromeDriver 服务对象
service = webdriver.chrome.service.Service(executable_path=chrome_path)

# 创建 WebDriver 对象
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get('https://baidu.com')

# 关闭浏览器
driver.quit()