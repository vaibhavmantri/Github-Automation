import sys
import os
import subprocess
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://github.com/login")
# Typing username
username = input("Enter the Email-Id/Username : ")
usernamebox = driver.find_element_by_xpath('//*[@id="login_field"]')
usernamebox.send_keys(username)
# typing password
password = input("Enter the Password : ")
passwordbox = driver.find_element_by_xpath('//*[@id="password"]')
passwordbox.send_keys(password)
loginbutton = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
loginbutton.click()
  # Creating a new repo button
repo_option = input("Do you wish to create a new Repo? [y] for yes and [n] for no : ")
if repo_option == 'y' or repo_option == 'yes' or repo_option == 'Yes' or repo_option == 'YES':
    new_repo_box = driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a')
    new_repo_box.click()
        # Writing name of repo
    repo_name = input("Enter the Repository name : ")
    repo_name_entry = driver.find_element_by_xpath('//*[@id="repository_name"]')
    repo_name_entry.send_keys(repo_name)
        # Public or Private Repo Option
    pub_pri_option = input("Do you wish to make the repository public or private?")
    if pub_pri_option == "private" or pub_pri_option == "Private":
        private_button = driver.find_element_by_xpath('//*[@id="repository_visibility_private"]')
        private_button.click()
    elif pub_pri_option == "public" or pub_pri_option == "Public":
        public_button = driver.find_elements_by_xpath('//*[@id="repository_visibility_private"]')
        public_button.click()
        # create_repo = driver.find_element_by_id('repository_auto_init')
        # create_repo.click()
    confirm_repo = driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
    confirm_repo.submit()

elif repo_option == 'n' or repo_option == 'no' or repo_option == 'No' or repo_option == 'NO':
    exit()
# git init
# git add README.md
# git commit -m "first commit"
# git remote add origin https://github.com/vaibhavmantri1/+'{repo_name}+'.git'
# git push -u origin master
