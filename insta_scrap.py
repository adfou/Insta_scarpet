import json
from pprint import pprint
import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys 
import os
import pathlib
from subprocess import CREATE_NO_WINDOW
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
class Instagram:
  def __init__(self,username, password, scarp_username,number):
    self.username = username
    self.password = password
    self.scarp_username = scarp_username
    self.number = number
    self.scrol = round(number/11)
    self.list = 'list.txt'
    print("aaa")
    
  def Login(self):
    Options=uc.ChromeOptions()
    num_profile = 1000
    scrol =round(num_profile/11)
    #mobile_emulation = {"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}

    prefs = {"credentials_enable_service": False,
          "profile.password_manager_enabled": False,
          "extensions.ui.developer_mode": True
           }
    Options.add_experimental_option("prefs", prefs)
    self.driver = uc.Chrome(use_subprocess=True, version_main=107,options = Options, service_creationflags=CREATE_NO_WINDOW)
    wait = WebDriverWait(self.driver, 20)

    url = 'https://instagram.com'
    self.driver.get(url)
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))).click()
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys(self.username)
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))).click()
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))).send_keys(self.password)
    WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button'))).click()
    time.sleep(5)
  
  def send_msg(self,msg,list):
    self.driver.get('https://www.instagram.com/direct/new/')
    time.sleep(3)
    #not now 
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))).click()
    file = open(list, 'r')
    Lines = file.readlines()
    for Line in Lines :
      try:
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input'))).send_keys(str(Line))
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div'))).click()
        time.sleep(1)                                                                         
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button'))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'))).send_keys(msg)
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'))).send_keys(Keys.ENTER)
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button/div'))).click()
        time.sleep(0.5)  
      except:
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input'))).clear()


  def scarp(self):
    self.driver.get('https://www.instagram.com/{}/followers/?hl=fr'.format(self.scarp_username))
    element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')))
   
    for n in range(1,self.scrol+1):
      time.sleep(2)
      try:
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)
      except:
        pass

    with open (self.list,"w") as f :
      for num in range(1,self.number+1):                                        
          list=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{}]/div[2]/div[1]/div/div/span/a/span/div'.format(num)) 
          print(num) 
          print(list.text)
          f.write("{}\n".format(list.text))
       
      time.sleep(5)
      self.driver.quit()

  
print("fffffffffff")                                 
user = Instagram("n_a_r_c_oss",'fb145723',"fleen.fan.off",1000)
user.Login()
user.scarp()





 #/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{}]/div[2]/div/div/div/span/a/span/div 
   
