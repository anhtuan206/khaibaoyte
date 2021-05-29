import time
from selenium import webdriver

hovaten = "Phan Anh Tuấn"
eoffice = "tuanpa2"
sodienthoai = "0906307547"

#Form EVNCPC
web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/1XVU12Awt8ztEMggZLnuGnBblYFcvH-p17JTGa_U6840/viewform?edit_requested=true')
time.sleep(3)

#name
answer1 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
answer1.send_keys(hovaten)
# time.sleep(2)

#1991
answer2 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
answer2.send_keys('Không')
#time.sleep(2)

#1982
answer3 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
answer3.send_keys('Không')
#time.sleep(2)

#1996
answer4 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
answer4.send_keys('Không')
#time.sleep(2)

#1995
answer5 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')
answer5.send_keys('Không')
#time.sleep(2)

#1986
answer6 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea')
answer6.send_keys('Không')
#time.sleep(2)

#1998
answer7 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea')
answer7.send_keys('Không')
#time.sleep(2)

#1995
answer8 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div[2]/textarea')
answer8.send_keys('Không')
#time.sleep(2)

#1939
answer9 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div[2]/textarea')
answer9.send_keys('Không')
#time.sleep(2)

#1991
answer9 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div[2]/textarea')
answer9.send_keys('Không')
#time.sleep(2)

#benh nhan khac
answer9 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div[2]/textarea')
answer9.send_keys('Không')
#time.sleep(2)

submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
submit.click()
time.sleep(3)

web.close()

#From CPCIT
web1 = webdriver.Chrome()
web1.get('https://docs.google.com/forms/d/e/1FAIpQLSdYXKTMQdRfOoHGPCwgL-Ro5T7EwGGJBoe7nuaaJk1NBL4z6A/viewform')
time.sleep(3)

# web1.execute_script("window.scrollTo(0, 1500)") 
# time.sleep(3)


#Ten TK eoffice
answer10 = web1.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
answer10.send_keys(eoffice)
#time.sleep(2)

#SDT
answer11 = web1.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
answer11.send_keys(sodienthoai)
#time.sleep(2)

#Duong Tinh
answer12 = web1.find_element_by_xpath('//*[@id="i18"]/div[3]/div')
answer12.click()
#time.sleep(2)

#Nhom
answer13 = web1.find_element_by_xpath('//*[@id="i34"]/div[3]/div')
answer13.click()
#time.sleep(2)

#Dien dai
answer14 = web1.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea')
answer14.send_keys('không')
#time.sleep(2)

submit1 = web1.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
submit1.click()
time.sleep(3)

web1.close()