#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get('http://web.skylongtech.com/web/dist/#/index')
#driver.maximize_window()

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get('http://wap.api-bc-1.com/wap/dist/#/AppIndex')
driver.maximize_window()
driver.send_keys(Keys.F12)
time.sleep(5)
driver.find_element_by_name('id').send_keys('joeuse1010')
driver.find_element_by_name("password").send_keys('a123456')
time.sleep(2)
driver.find_element_by_class('btn loginbtn').click()
time.sleep(10)
#while True:
 #current_time = time.localtime(time.time())
 #if((current_time.tm_min%20 == 0) and (current_time.tm_sec == 0)):
 #driver.refresh()
 #time.sleep(10)
 #driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div[1]/div[2]/div/div[2]/span[1]").click()
 #elif((current_time.tm_hour == 18) and (current_time.tm_sec == 0)):
 #driver.close()
 #break