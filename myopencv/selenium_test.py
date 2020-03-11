
import time
import sys
from selenium import webdriver 

chrome = webdriver.Chrome(executable_path='D:\\workspace\\automation\\chromedriver_win32\\chromedriver.exe') 
chrome.implicitly_wait(3) 
chrome.get('http://www.naver.com')
chrome.implicitly_wait(3) 
chrome.save_screenshot("test.png")
chrome.save_screenshot("test.jpg")
chrome.close()
