import sys
import os
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://github.com/login")


    #Typing username
username = input("Enter the Email-Id/Username : ")
usernamebox = driver.find_element_by_xpath('//*[@id="login_field"]')
usernamebox.send_keys(username)
    #typing password
password = input("Enter the Password : ")
passwordbox = driver.find_element_by_xpath('//*[@id="password"]')
passwordbox.send_keys(password)
loginbutton = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
loginbutton.click()
    #Creating a new repo button
repo_option = input(("Do you wish to create a new Repo? [y] for yes and [n] for no : "))
if repo_option == 'y':
    new_repo_box = driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a')
    new_repo_box.click()
        #Writing name of repo
    repo_name = input("Enter the Repository name : ")
    repo_name_entry = driver.find_element_by_xpath('//*[@id="repository_name"]')
    repo_name_entry.send_keys(repo_name)
    #Public or Private Repo Option
    pub_pri_option = input("Do you wish to make the repository public or private?")
    if pub_pri_option == "private" or pub_pri_option == "Private":
        private_button = driver.find_element_by_xpath('//*[@id="repository_visibility_private"]')
        private_button.click()
    elif pub_pri_option == "public" or pub_pri_option == "Public":
        public_button  = driver.find_elements_by_xpath('//*[@id="repository_visibility_private"]') 
        public_button.click()
    #Adding README.md file
    add_readme = driver.find_elements_by_id('repository_auto_init')
    add_readme.click()
    #Creating the repository
    create_repo = driver.find_element_by_css_selector('#new_repository > div.js-with-permission-fields > button')
    create_repo.click()
elif repo_option == 'n':
    exit()

    # <input type="checkbox" value="1" name="repository[auto_init]" id="repository_auto_init">

