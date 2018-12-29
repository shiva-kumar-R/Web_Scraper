from bs4 import BeautifulSoup
from selenium import webdriver


url = 'https://www.nyse.com/quote/XNYS:'

text = input()
query = text.split(':')[0]

chrome_driver = "C:/Users/Shivakumar r/Desktop/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(url+query)

posts = driver.find_element_by_class_name('d-dquote-symbol')
time = driver.find_element_by_class_name('d-dquote-time')

print(posts.text)
print(time.text)
