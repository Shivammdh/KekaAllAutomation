import time
from pprint import pprint

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


menu=driver.find_element(By.CSS_SELECTOR,".ic-person.sidebar-list-icon")
print(menu.is_displayed())
action.move_to_element(menu).perform()
wait=WebDriverWait(driver,60)
button=wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Attendance')]")))
print(button.is_displayed())
action.move_to_element(button).click().perform()

print(driver.current_url)

all_loged=driver.find_elements(By.CSS_SELECTOR,".d-flex.align-items-center.justify-content-between.px-16.py-12.border-bottom.on-hover")

print(len(all_loged))
l=[]
for log in all_loged:
    txt=log.text
    l1 = txt.split("\n")
    if (l1[0] == 'No Time Entries Logged'):
        l2 = l1[1].split(",")
        l3 = l2[0].split(" ")
        l.append(l3[1])
    # if newtxt=='No Time Entries Logged':
    #   log.find_element(By.CSS_SELECTOR,"div .w-38").click()
l.sort()
pprint(l)
driver.find_element(By.XPATH,"//a[contains(text(),'Work From Home')]").click()
driver.find_element(By.CSS_SELECTOR,".start-date").click()
dates=driver.find_elements(By.CSS_SELECTOR,"td[role='gridcell']")
count=len(dates)
for i in range(count):
    t=driver.find_elements(By.CSS_SELECTOR,"td[role='gridcell']")[i].text
    if t.lower()==l[0].lower():
        print(t)
        driver.find_elements(By.CSS_SELECTOR,"td[role='gridcell']")[i].click()
        break

for j in range(count):
    td=driver.find_elements(By.CSS_SELECTOR,"td[role='gridcell']")[j].text

    if td.lower()==l[-1].lower():
        print(td)
        driver.find_elements(By.CSS_SELECTOR,"td[role='gridcell']")[j].click()
        break

txt_area=driver.find_element(By.CSS_SELECTOR,"div[class='form-group'] textarea")
#txt_area.click()
txt_area.send_keys("WFH Due to covid")
#driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary").click()
print(driver.current_url)







