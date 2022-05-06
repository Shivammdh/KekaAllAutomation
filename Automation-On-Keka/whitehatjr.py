import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://whitehatjr.darwinbox.in/tasksApi/GetTasks")
driver.find_element(By.CSS_SELECTOR,"input[id='username']").send_keys("WHJREXP-0730")
driver.find_element(By.CSS_SELECTOR,"label.sc-gzOgki.geMbJY").click()
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("synapse@199801111")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(25)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"button.sc-kpOJdX.cHUTBb").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".db-dashboard.dashboard-circle").click()
driver.find_element(By.XPATH,"//div[@class='col-xs-12 plr-12']/div[2]").click()
time.sleep(5)
wait = WebDriverWait(driver, 120)
e=wait.until(EC.presence_of_element_located((By.ID,"a6218e142a01fd_a62219d3753a67_a62219d3d21e47")))
print(e)
e.click()
#driver.find_element(By.ID,"a6218e142a01fd_a62219d3753a67_a62219d3d21e47").click()
time.sleep(3)
all_el=driver.find_elements(By.XPATH,"//label[contains(text(),'Yes')]")
for el in all_el:
    el.click()
# Xpath for Sales : //div[contains(text(),'Sales')]