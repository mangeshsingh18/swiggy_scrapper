# Necesssory Modules Import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from openpyxl import Workbook, load_workbook
import time
import pandas as pd


# User Input
Mobile_No = input("Please Enter Your Number :- ")
Location = input("Please Enter Your Location :- ")

# Chrome Driver Location
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.maximize_window()     # To Maximize The Window

# Website link
driver.get("https://www.swiggy.com/")     
print(driver.title)
time.sleep(2)

# For Login Page 
login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@class="x4bK8"]')))
time.sleep(1)
login.click()

login_phone = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mobile"]')))
time.sleep(1)
login_phone.click()
time.sleep(1)
login_phone.send_keys(f"{Mobile_No}")
time.sleep(1)

login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@class="a-ayg"]')))
time.sleep(1)
login_btn.click()
time.sleep(2)

Otp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="otp"]')))
time.sleep(1)
Otp.click()

# Otp for Login In Swiggy
Otp_input = input("Enter the OTP Number :- ")
time.sleep(1)
Otp.send_keys(f"{Otp_input}")
time.sleep(1)

verify_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@class="a-ayg"]')))
time.sleep(1)
verify_btn.click()
time.sleep(2)

# Your Location
location = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="location"]')))
time.sleep(1)
location.click()
time.sleep(1)
location.send_keys(f"{Location}")
time.sleep(1)

loc_click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[2][@class="_2W-T9"]')))
time.sleep(1)
loc_click.click()
time.sleep(1)

# Selecting Category from Low to High
low_to_high = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_restaurants"]/div/div[1]/div/div/div/div[2]/div[4]')))
time.sleep(1)
low_to_high.click()
time.sleep(1)

items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="_1j_Yo"]')))
time.sleep(2)
length = len(items)
print(len(items))

item = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="_1gURR"]')))
time.sleep(1)

item_price = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="nVWSi"]')))
time.sleep(1)

restaurant = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="nA6kb"]')))
time.sleep(1)

timing = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="_3Mn31"]/div[3]')))
time.sleep(1)

discount = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="Zlfdx"]')))
time.sleep(1)

rating = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="_3Mn31"]/div[1]/span[2]')))
time.sleep(1)

Item_Name = []
Item_Price = []
Restaurant_Name = []
Timing = []
Discount = []
Rating = []

for n,p,r,t,d,rt in zip(item, item_price,restaurant,timing,discount,rating) :
    Item_Name.append(n.text) 
    Item_Price.append(p.text) 
    Restaurant_Name.append(r.text) 
    Timing.append(t.text) 
    Discount.append(d.text)
    Rating.append(rt.text)


data = {'ITEM_NAME': Item_Name, 'ITEM_PRICE': Item_Price, 'RESTAURENT_NAME': Restaurant_Name, 'TIMING': Timing, 'DISCOUNT': Discount, 'RATING': Rating}

print(data)


# saving the dataframe
df = pd.DataFrame(data)
df.to_excel(r"F:\BeautifulSoup\swiggy_scrapper\swiggy.xlsx")

print("Done!!!!!!")

 