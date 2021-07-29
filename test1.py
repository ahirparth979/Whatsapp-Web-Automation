'''
@author: Parth Ahir
'''


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
import pandas as pd


driver = None
Link = "https://web.whatsapp.com/"
wait = None

def whatsapp_login():
    global wait, driver, Link
    chrome_options = Options()
    chrome_options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 2)
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB IF DISPLAYED")
    driver.get(Link)
    driver.maximize_window()
    print("QR CODE SCANNED")
    
def send_message(name,msg):
    user_group_xpath = '//span[@title = "{}"]'.format(name)
    flag = True
    sleep(15)
    while(flag):
        try:
            user = wait.until(EC.presence_of_element_located((By.XPATH, user_group_xpath)))
            user.click()
            flag = False
        except Exception:
            driver.execute_script("document.getElementById('pane-side').scrollBy({top: window.innerHeight, behavior: 'smooth'})")
            flag = True

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys(msg)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    print("Message send successfully to {}.".format(name))

if __name__ == "__main__":
    
    today = datetime.datetime.now().strftime("%x")
    file = pd.read_csv(r"E:\Parth\eclipse-workspace\Birthday Wisher\birthday_list.csv")
    # Let us login and Scan
    print("Now, Web Page Open")
    whatsapp_login()
    for i, j in file.iterrows(): 
        if(j[1] == today):
            name = j[0]
            msg = "Happy Birthday {}!!!".format(j[0])
            
            send_message(name,msg)

    sleep(10)
    driver.close()
    driver.quit()