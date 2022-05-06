import time
from pprint import pprint
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrom_opt=webdriver.ChromeOptions()
chrom_opt.add_argument('headless')
driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://app.keka.com/Account/KekaLogin?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fresponse_type%3Dcode%26client_id%3D987cc971-fc22-4454-99f9-16c078fa7ff6%26state%3DVX5RdmlpNUpwV3UxX1BEZGFUdUJ-U25pUzQxaU5JNG51bmJObUN5blVUbE0z%26redirect_uri%3Dhttps%253A%252F%252Fmsys.keka.com%26scope%3Dopenid%2520offline_access%2520kekahr.api%2520hiro.api%26code_challenge%3DzNH3gnY_gwcfdLCptVAISxHcXAaJcz3-sig495pogOk%26code_challenge_method%3DS256%26nonce%3DVX5RdmlpNUpwV3UxX1BEZGFUdUJ-U25pUzQxaU5JNG51bmJObUN5blVUbE0z")

# set the value in value atribute
vd=driver.find_element(By.CLASS_NAME,"form-control")
driver.execute_script("arguments[0].value='msys';",vd)

#send the email and password to these fields
driver.find_element(By.ID,"email").send_keys("ssharma@msystechnologies.com")

#driver.execute_script("document.getElementsByClassName('form-control').setAttribute('value', 'msys')")
driver.find_element(By.ID,"password").send_keys('Shivam@0105')
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

action=ActionChains(driver)


menu=driver.find_element(By.CSS_SELECTOR,".ic-org.sidebar-list-icon")

action.move_to_element(menu).click().perform()
driver.find_element(By.CSS_SELECTOR,".filter-label").click()
driver.find_element(By.CSS_SELECTOR,"span[title='MSys Pune']").click()
time.sleep(3)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
allemp=driver.find_elements(By.XPATH,"//div[@class='col-default-3']/div/div/div")
print(len(allemp))
emplist=[]
for emp in allemp:
    empdict={}
    empdict['Name']=emp.find_element(By.XPATH,"div/h4").text
    empdict['Post']=emp.find_element(By.XPATH,"span[1]").text
    location=emp.find_element(By.XPATH,"span[3]").text.split(":")
    empdict['Location']=location[1]
    emplist.append(empdict)

df=pd.DataFrame(emplist)
df.to_csv("EmpData.csv")
driver.close()

#employee name: //div[@class='col-default-3']/div/div/div/div/h4
#employee Desnigation: //div[@class='col-default-3']/div/div/div/span[1]
#location: //div[@class='col-default-3']/div/div/div/span[3]