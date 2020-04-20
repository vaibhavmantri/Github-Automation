from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://github.com/login")
#Typing username
username = input("Enter the Email Id : ")
usernamebox = driver.find_element_by_xpath('//*[@id="login_field"]')
usernamebox.send_keys(username)
#typing password
password = input("Enter the Password : ")
passwordbox = driver.find_element_by_xpath('//*[@id="password"]')
passwordbox.send_keys(password)
#
loginbutton = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
loginbutton.click()
#Creating a new repo button
repo_option = input(("Do you wish to create a new Repo? [y] for yes and [n] for no"))
if repo_option == 'y':
    new_repo_box = driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a')
    new_repo_box.click()
    #Writing name of repo
    repo_name = input("Enter the Repository name : ")
    repo_name_entry = driver.find_element_by_xpath('//*[@id="repository_name"]')
    repo_name_entry.send_keys(repo_name)
    #Creating the repository
    create_repo = driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
    create_repo.click()
elif repo_option == 'n':
    exit()

