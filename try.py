import time
import selenium.common
import numpy as np
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chromium.options import ChromiumOptions
from bs4 import BeautifulSoup as bs
from selenium.webdriver.remote.webdriver import By
import argparse
base_url = 'https://cgifederal.secure.force.com'

def reset_chrome(driver, chrome_options):
    time.sleep(5)
    # handle = driver.current_window_handle
    # driver.service.stop()
    # time.sleep(1)
    # driver = webdriver.Chrome(options=chrome_options)
    # driver.switch_to.window(handle)


def is_login_page_loading_completed(driver):
    try:
        driver.find_element(By.ID,
            "Registration:SiteTemplate:theForm:username"
        )
    except selenium.common.exceptions.NoSuchElementException as e:
        print(f"当前页面仍未找到用户名输入栏, url={driver.current_url}")
        return False
    except Exception as e:
        print(f"其他报错: {e}, url={driver.current_url}")
        return False
    return True

def my_login(driver, chrome_options, cracker, uri, info='', max_try=50):

    print('login', info)
    target_url = base_url + uri
    print(f"进入login, 当前正在访问的url: {target_url}")
    driver.get(target_url)

    while True:
        if not is_login_page_loading_completed(driver):
            max_try -= 1
            if max_try == 0:
                print(f"所有重试次数={max_try}已使用，仍未检测到目标输入框，不再继续等待，直接退出")
                return
            else:
                print(f"当前页面上还没有找到用户名输入框, 重置浏览器, 休息几秒...等待下次检测")
                reset_chrome(driver, chrome_options)
        else:
            break

    username = ''.join([chr(np.random.randint(26) + ord('a'))
                        for _ in range(15)]) + "@gmail.com"
    print(f"username: {username}")
    driver.find_element(By.ID,
        "Registration:SiteTemplate:theForm:username"
    ).send_keys(username)
    firstname = ''.join(np.random.permutation(' '.join('abcdef').split()))
    print(f"firstname: {firstname}")
    driver.find_element(By.ID,
        "Registration:SiteTemplate:theForm:firstname").send_keys(
        firstname)
    driver.find_element(By.ID,
        "Registration:SiteTemplate:theForm:lastname").send_keys(
        ''.join(np.random.permutation(' '.join('qwerty').split())))
    password = ''.join(np.random.permutation(' '.join('12345qwert').split()))
    print(f"password: {password}")
    driver.find_element(By.ID,
        "Registration:SiteTemplate:theForm:password").send_keys(password)
    driver.find_element(By.ID,
        "Registration:SiteTemplate:theForm:confirmPassword"
    ).send_keys(password)
    driver.find_element(By.XPATH, '//input[@name="Registration:SiteTemplate:theForm:j_id169"]').click()
    print(f"已完成勾选")
    # while True:
    #     html = bs(driver.page_source, 'html.parser')
    #     raw = html.find_all(id='Registration:SiteTemplate:theForm:theId')
    #     raw = raw[0].attrs['src'].replace('data:image;base64,', '')
    #     img = base64.b64decode(raw)
    #     if len(img) > 0:
    #         break
    #     time.sleep(0.1)
    # gifname = 'try.gif'
    # open(gifname, 'wb').write(img)
    # open('gifname', 'w').write(gifname)
    # captcha = cracker.solve(img).replace('1', 'l').lower()
    # if len(captcha) == 0:
    #     open('state', 'w').write(
    #         '自动识别服务挂掉了，请到<a href="https://github.com/Trinkle23897/'
    #         'us-visa">GitHub</a>上提issue')
    #     # exit()
    # driver.find_element_by_id(
    #     "Registration:SiteTemplate:theForm:recaptcha_response_field"
    # ).send_keys(captcha)
    driver.find_element(By.ID,
        "Registration:SiteTemplate:theForm:submit").click()
    print(f"已点击提交")
    time.sleep(6)
    # if driver.page_source.find('无法核实验证码') == -1:
    #     os.system('mv %s log/%s.gif' % (gifname, captcha))
    #     break
    # else:
    #     if not os.path.exists('fail'):
    #         os.makedirs('fail')
    #     os.system('mv %s fail/%s.gif' % (gifname, captcha))
    #     if hasattr(cracker, 'wrong'):
    #         cracker.wrong()

def postprocess(raw):
    if raw == []:
        return "/"
    m = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December'].index(
        raw[1]) + 1
    d = raw[2][:-1]
    y = raw[3][:-1]
    return '{}/{}/{}'.format(y, m, d)
def b_visa(driver):
    new_page_url = base_url + '/selectvisatype'
    print(f"进入新页面: {new_page_url}")
    driver.get(new_page_url)
    driver.find_element(By.ID, "j_id0:SiteTemplate:theForm:ttip:2").click()
    driver.find_element(By.XPATH, "//div[3]/div[3]/div/button/span").click()
    driver.find_element(By.XPATH, '//input[@name="j_id0:SiteTemplate:theForm:j_id176"]').click()
    name = ['北京', '武汉', '广州', '上海', '沈阳']
    s = {'time': time.strftime('%Y/%m/%d %H:%M', time.localtime())}
    cur = time.strftime('%Y/%m/%d', time.localtime())
    print(s['time'])
    for i in range(len(name)):
        n = name[i] + '-' + cur
        n2 = name[i] + '2-' + cur
        driver.get(base_url + '/SelectPost')
        time.sleep(5)
        driver.find_element(By.ID, "j_id0:SiteTemplate:j_id112:j_id165:{}".format(i)).click()
        driver.find_element(By.XPATH, '//input[@name="j_id0:SiteTemplate:j_id112:j_id169"]').click()
        try:
            driver.find_element(By.ID, "j_id0:SiteTemplate:j_id109:j_id162:0").click()
            driver.find_element(By.XPATH, '//input[@name="j_id0:SiteTemplate:j_id109:j_id166"]').click()
        except:
            pass
        driver.find_element(By.XPATH, "(//input[@id='selectedVisaClass'])[2]").click()
        driver.find_element(By.XPATH, '//input[@name="j_id0:SiteTemplate:theForm:j_id178"]').click()
        result = bs(driver.page_source, 'html.parser').findAll(
            class_='leftPanelText')
        if len(result):
            result = result[0].text.split()[1:]
            print(f"result={result}")
        s[n] = s[n2] = postprocess(result)
        # if s[n] != '/':
        #     path = 'B/' + n.replace('-', '/')
            # os.makedirs('/'.join(path.split('/')[:-1]), exist_ok=True)
            # open(path, 'a+').write(s['time'].split(' ')
            #                        [-1] + ' ' + s[n] + '\n')
        print('B1/B2', n, s[n])
        time.sleep(3)


parser = argparse.ArgumentParser()
parser.add_argument('--secret', type=str, default='')
# parser.add_argument('--proxy', type=int, default=7890)#1080)
args = parser.parse_args()

# chrome_options = uc.ChromeOptions()#Options()
chrome_options = Options()#ChromiumOptions()
# chrome_options.add_experimental_option("detach", True)
# if len(args.secret) == 0:
# cracker = args
# cracker.solve = lambda x: input('Captcha: ')
cracker = None
# else:
#     cracker = Captcha(args.secret, 1080)
#     chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument(
#     '--proxy-server=socks5://127.0.0.1:%d' % args.proxy)
# chrome_options.add_argument('--disable-dev-shm-usage')

# 参考: https://zhuanlan.zhihu.com/p/624019626
# chrome_options.add_experimental_option("detach", True)  # 不要自动关闭浏览器
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # 这里添加一些启动的参数
# chrome_options.add_argument('--window-size=720,720')    # 设置浏览器窗口大小
# chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 取消chrome受自动控制提示
# chrome_options.add_argument("start-maximized")


driver = uc.Chrome(options=chrome_options, use_subprocess=True)

uri = '/SiteRegister?country=China&language=zh_CN'
info = "China Mainland"

chrome_options = None

# target_url = base_url + '/selectvisatype'
# print(f"target_url = {target_url}")
# driver.get(target_url)
my_login(driver, chrome_options, cracker, uri=uri, info=info)
b_visa(driver)