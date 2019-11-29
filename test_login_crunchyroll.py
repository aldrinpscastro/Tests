#!/usr/bin/env python3
from selenium import webdriver
from time import sleep
browser = webdriver.Chrome(executable_path='/home/reginaldo/Programas/getpasscrunchyrolloncomments/chromedriver')
browser.get('https://www.crunchyroll.com/coupon_redeem?code=5XVS8857T8U')
#browser.find_elements_by_class_name('userpanel-item')[0].click()
sleep(2)
browser.find_elements_by_id('login_form_name')[0].send_keys('aldrinpscastro')
browser.find_elements_by_id('login_form_password')[0].send_keys('ItAchI!(($!(($')
browser.find_elements_by_id('login_submit_button')[0].click()
sleep(2)
if len(browser.find_elements_by_class_name('error-message')) == 0:
	browser.find_elements_by_class_name('submit')[0].click()
	print('O passe ainda não foi resgatado!')
else:
	browser.quit()
	print('O passe já foi resgatado!')
