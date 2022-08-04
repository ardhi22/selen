from selenium import webdriver
from time import sleep
import os

url = ["http://gestyy.com/edWJbW", "http://gestyy.com/edWJn9", "http://gestyy.com/edWJWz", "http://gestyy.com/edWJWL", "http://gestyy.com/edWJXA", "http://gestyy.com/edWJCO"]

print("Memulai sistem!")
while True:
	#Ronde1
	os.chdir("C:/Program Files/NordVPN")
	os.system("nordvpn -c")
	os.chdir("C:/Users/Sahal/Desktop")
	driver = webdriver.Chrome()
	driver.get(url[0])
	sleep(10)
	driver.get(url[0])
	sleep(2)
	driver.get(url[1])
	sleep(10)
	driver.get(url[1])
	sleep(2)
	driver.get(url[2])
	sleep(10)
	driver.get(url[2])
	sleep(2)
	driver.quit()
	sleep(5)
	#Ronde2
	os.chdir("C:/Program Files/NordVPN")
	os.system("nordvpn -c")
	os.chdir("C:/Users/Sahal/Desktop")
	driver = webdriver.Chrome()
	driver.get(url[3])
	sleep(10)
	driver.get(url[3])
	sleep(2)
	driver.get(url[4])
	sleep(10)
	driver.get(url[4])
	sleep(2)
	driver.get(url[5])
	sleep(10)
	driver.get(url[5])
	sleep(2)
	driver.quit()
	sleep(5)
print("All is done!")
