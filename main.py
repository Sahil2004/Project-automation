import sys, os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

directory = os.getcwd() #Get the program directory
username = "" #Username (Put your username)
pwd = "" #Password (Put your password)

def cli_interaction_one():
    os.chdir("your/path/Current Projects") #Navigating to the projects folder
    os.system(f'mkdir "{sys.argv[1]}"') #Making the folder
    os.chdir(f'your/path/Current Projects/{sys.argv[1]}')
    os.system("echo '' >> Readme.md") #Making the readme file (works only in windows, different command for other OS)
    os.system("git init") #Initialize git repo
    os.system("git add .") #Adding all the stuff
    os.system('git commit -m "First commit"') #Making the first commit    

def browser_interaction():
    # For this to work, you must already be signed in as it will skip the sign in process.
    os.chdir(directory) #Get the executable directory to access the geckodriver
    driver = webdriver.Firefox(executable_path='geckodriver.exe') #Using firefox automation
    driver.get("https://github.com/new") #Visiting github new page (page for making repo)
    element = driver.find_element_by_id("login_field") #Get the login field
    element.send_keys(username) #Sending username
    element = driver.find_element_by_id("password") #Get the password field
    element.send_keys(pwd) #Send the password keys
    element.send_keys(Keys.RETURN) #Sending enter key after filled
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'repository_name'))) #Wait for 5 seconds to load the page
    element = driver.find_element_by_id("repository_name") #Getting the input field where the repo name has to filled
    element.send_keys(sys.argv[1]) #Sending repo name keys
    time.sleep(5) #Wait for 5 seconds
    element.send_keys(Keys.RETURN) #Sending enter key after filled
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'empty-setup-clone-url'))) #Wait 15 seconds to load the page
    global repo #Defining the global variable
    repo = driver.current_url #Changing the global variable value to the url of repo

def cli_interaction_two():
    os.chdir(f'your/path/Current Projects/{sys.argv[1]}') #Changing the working directory to configure it further
    os.system(f'git remote add origin {repo}.git') #Adding the remote repo
    os.system("git push -u origin master") #Pushing the first commit to the repo in the master branch
    os.system(f'explorer "your/path/Current Projects/{sys.argv[1]}"') #open file explorer in the project directory
    os.system("code .") #Opening VS Code (Command for opening the code editor)

def main():
    cli_interaction_one() #Making an offline repo on the system.
    browser_interaction() #Making an online repo on github
    cli_interaction_two() #Adding the remote repo

if __name__ == '__main__':
    main()