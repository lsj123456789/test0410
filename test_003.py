# @Author:lsj
# @version V1.0
# -*- coding:UTF-8 -*-

from appium import webdriver
import time
caps={}
caps['platformName'] = 'Android'  # 平台名称
caps['platformVersion'] = '5.1.1'  # 设备系统版本号
caps['deviceName'] = '127.0.0.1:62001'  # 设备名称（可以随意写取adb devices连接的第一台设备）
caps['appPackage'] = 'com.youba.calculate'  # 包名 adb shell pm list package -3 查看第三方包名
caps['appActivity'] = '.MainActivity'
# adb shell dumpsys window windows |dindstr mFocusedApp

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
# 关闭当前操作
driver.close_app()
# 启动应用
driver.start_activity('com.youba.calculate','.MainActivity')

time.sleep(3)
# 计算1+2=3
# 按“1”
driver.find_element_by_id('com.youba.calculate:id/btn_one').click()
# 按“+”
driver.find_element_by_id('com.youba.calculate:id/btn_plus').click()
# 按“2”
driver.find_element_by_id('com.youba.calculate:id/btn_two').click()
# 按“=”
driver.find_element_by_id('com.youba.calculate:id/btn_equal').click()

# 加入断言：判断是否是3
# 获取结果文本
res_text = driver.find_element_by_id('com.youba.calculate:id/tv_display').text
assert res_text == '3'

print("结果正确！！！")

time.sleep(3)
driver.quit()