from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.HttpUtils import HttpUtils
options = Options()
httpUtils = HttpUtils()
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path="E:/配置文件/driver/chromedriver_74.exe", )
driver.get(
    'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F%3Fcu%3Dtrue%26utm_source%3Dbaidu-pinzhuan%26utm_medium%3Dcpc%26utm_campaign%3Dt_288551095_baidupinzhuan%26utm_term%3D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_18227775daa94542814e72d4fbe192f1')
userLogin = driver.find_elements_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]")[0]
userLogin.click()
loginname = driver.find_element_by_id("loginname")
loginname.send_keys("979982272@qq.com")
nloginpwd = driver.find_element_by_id("nloginpwd")
nloginpwd.send_keys("your_pwd")
loginsubmit = driver.find_element_by_id("loginsubmit")
loginsubmit.click()

