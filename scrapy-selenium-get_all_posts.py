
import os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException    
import csv



path = os.path.dirname(__file__) 
driver = webdriver.Chrome(executable_path=os.path.join(path, "selenium/chromedriver"))


username = input("Digite o seu usuário do Instagram, sem a arroba, e aperte < ENTER >.\n")
password = input("Digite a senha do Instagram, e aperte < ENTER >.\n")
conta = input("Digite o úsuario que deseja capturar os dados, e aperte < ENTER >.\n")


url_base = "https://www.instagram.com/"
url_login = url_base+"accounts/login/"
url_profile = url_base+conta

#fazer login
driver.get(url_login)

sleep(2)
username_field = driver.find_element_by_name('username')
password_field = driver.find_element_by_name('password')

username_field.send_keys(username)
password_field.send_keys(password)

sleep(1)
driver.find_element_by_xpath("//button[contains(.,'Entrar')]").click()

driver.get(url_profile)

sleep(2)
user_posts = []
user_posts_code = []

#Acessar oagina que deseja listar todas as postagens
posts = driver.find_elements_by_xpath("//*[contains(@class, 'v1Nh3 kIKUG  _bz0w')]")
count = 0
last_location = {'x': -1, 'y': -1}
next_location = {'x': 0, 'y': 0}


with open('insta_output.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	
	#TODO encontrar uma forma efetiva de finalizar o processo	    
	# while last_location != next_location:
	while True:
		q = len(posts)
		print('%d elements', q)
		if q > 0:
			last_item = posts[q-1]
			for post in posts:
				print('#%d:', count)

				# user_posts.append(post)
				try:
					code = post.find_element_by_tag_name("a")
					print("code: %s", code)
					print (code.get_attribute("href"))
					count += 1
					writer.writerow([code.get_attribute("href")])

				except NoSuchElementException:
					pass
				# code = post.find_element_by_tag_name("a")
				# user_posts_code.append(code)
				# print(count)
				# print(post)
				# write_csv('insta_output.csv',[post.get_attribute('innerHTML')])
			last_location = next_location
			next_location =  last_item.location_once_scrolled_into_view
			print(next_location)
			#heart.click()
			#time.sleep(2)
		sleep(2)
		posts = driver.find_elements_by_xpath("//*[contains(@class, 'v1Nh3 kIKUG  _bz0w')]")



