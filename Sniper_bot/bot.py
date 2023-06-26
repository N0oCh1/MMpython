import requests_html 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from requests_html import HTMLSession, AsyncHTMLSession

url = "https://www.google.com/"

def main():
    
    stoks = check()
    browser(stoks)
    

def check():
    session = HTMLSession()
    stoks = False
    content = session.get(url)
    buy_zone = content.html.find("#APjFqb")
    if len(buy_zone) > 0: 
        print("stoks")
        stoks = True
        return stoks
    else:
        return print("no hay stock")
    

def browser(stoks):
    print(stoks)
    if stoks:
        driver = webdriver.Firefox()
        driver.get(url)
        textarea = driver.find_element(By.TAG_NAME ,"textarea")
        sleep(5)
        textarea.send_keys("gatos", Keys.ENTER)
        sleep(5)
        driver.find_element(By.CLASS_NAME, "yuRUbf").click()
        input()
        



if __name__ == '__main__':
    main()