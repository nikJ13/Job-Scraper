# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 22:39:04 2023

@author: niket
"""

import selenium
from selenium import webdriver as wb
import pandas as pd
import time
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import imaplib
import email
from email.header import decode_header


def main():
    #driver = wb.Chrome(r"C:\Niket\Job Scraper\chromedriver-win64\chromedriver.exe")
    url = "https://www.linkedin.com"
    driver = wb.Chrome(r"C:\Niket\Job Scraper\chromedriver-win64\chromedriver.exe")
    driver.get(url)
    driver.maximize_window()
    #element = driver.find_element(By.XPATH,"//iframe")
    #print(element.get_attribute("src"))
    flag_login = authentication(driver)
    print(flag_login)
    time.sleep(5)
    flag_search = searchCompany(driver)
    print(flag_search)
    #h1_element = driver.find_element(By.TAG_NAME, "h1")
    #if h1_element.text == "Let's do a quick verification":
        #email_code(driver)
        
    #if(driver.find_elements(By.XPATH,"//form[@class='google-auth']")):
        
    # get geeksforgeeks.org
    #driver.get("https://www.geeksforgeeks.org/")
    
# get element 
    #element = driver.find_element(By.XPATH, "//form[input/@name ='search']")
 
# print complete element
    #print(element)

def authentication(driver):
    try:
        #finding the login element
        username = driver.find_element("id","session_key")
        #sending the keys for username
        username.send_keys("niketjaina4@gmail.com")
        time.sleep(2)
        #finding the keys for username
        password = driver.find_element("id","session_password")
        #sending the keys for password
        password.send_keys("manafamily404")
        time.sleep(2)
        #finding submit button
        driver.find_element(By.CSS_SELECTOR,"[data-id='sign-in-form__submit-btn']").click()
        #driver.find_element(By.CLASS_NAME,"btn-md btn-primary flex-shrink-0 cursor-pointer sign-in-form__submit-btn--full-width").click()
        return "yes"
    except Exception as e:
        return f"nope, the error is {e}"
    
def email_code(driver):
    # Gmail IMAP settings
    email_address = "niketjaina4@gmail.com"
    password = "maanfamm@0606"
    
    # Connect to Gmail IMAP server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_address, password)
    
    # Select the mailbox you want to access (e.g., 'inbox')
    mail.select("inbox")
    
    # Search for all emails in the 'inbox'
    status, messages = mail.search(None, "ALL")
    message_ids = messages[0].split()
    
    # Fetch the latest email
    latest_message_id = message_ids[-1]
    status, msg_data = mail.fetch(latest_message_id, "(RFC822)")
    raw_email = msg_data[0][1]
    
    # Parse the raw email content
    msg = email.message_from_bytes(raw_email)
    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding or "utf-8")
    print("Subject:", subject)

def searchCompany(driver):
    try:
        #driver.find_element(By.CSS_SELECTOR,"[id='ember7']").click()
        # driver.find_element(By.CSS_SELECTOR,"[class='search-global-typeahead__collapsed-search-button']").click()
        # time.sleep(2)
        # company_name = "Microsoft"
        # company_search = driver.find_element(By.CSS_SELECTOR,"[class='search-global-typeahead__input']")
        # company_search.send_keys(company_name)
        # company_search.send_keys(Keys.RETURN)
        # time.sleep(10)
        # a_tag = driver.find_element(By.CSS_SELECTOR,"[class='app-aware-link ']")
        # href_value = a_tag.get_attribute("href")
        # driver.get(href_value)
        company_name = "microsoft"
        driver.get(f"https://linkedin.com/company/{company_name}")
        time.sleep(5)
        #searching people
        driver.get(f"https://linkedin.com/company/{company_name}/people")
        time.sleep(5)
        #applying the filters
        region = "India"
        profession = "recruiter"
        search_people = driver.find_element(By.CSS_SELECTOR,"[id='people-search-keywords']")
        input_search = region+" "+profession
        search_people.send_keys(input_search)
        time.sleep(5)
        search_people.send_keys(Keys.RETURN)
        #scrolling down
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, 700)")
        #scroll_till = driver.find_element_by_class_name("artdeco-card org-people-profile-card__card-spacing org-people__card-margin-bottom")
        #driver.execute_script("arguments[0].scrollIntoView();", scroll_till)
        #getting the profiles
        time.sleep(10)
        #ul_element = driver.find_element(By.XPATH,"//ul[contains(@class,'display-flex list-style-none flex-wrap')]")
        ul_element = driver.find_element_by_xpath("//ul[contains(@class,'display-flex list-style-none flex-wrap')]")
        print(ul_element)
        li_elements = ul_element.find_elements_by_css_selector("li")
        #click on each list item
        for li_item in li_elements:
            li_item.click()
            div_ele = driver.find_element_by_xpath("//div[contains(@class,'pv-top-card-v2-ctas')]")
            first_button = div_ele.find_elements_by_xpath("//span[contains(@class,'artdeco-button__text')]")[0]
            print(first_button)
        return "yes"
    except Exception as e:
        return f"nope, the error is {e}"
    
def profileSelect(driver):
    try:
        driver.find_element(By.CSS_SELECTOR,"[id='ember14']").click()
    except Exception as e:
        return e

if __name__ == "__main__":
    main()

# filter
"""Skillset = ['Analysis','Python','SQL']
Skillset = [x.lower() for x in Skillset]
LL = 15       #lower limit of expected CTC
UL = 25       #upper limit of expected CTC
location = 'Bangalore'
location = location.lower().replace(" ","-")
role = 'Data Analyst'
role = role.lower().replace(" ","-")"""