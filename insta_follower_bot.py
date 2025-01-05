from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from random import choices
import random
import imaplib
import email
from email.header import decode_header

# Path to your ChromeDriver
chrome_driver = "/home/sujal/Downloads/chromedriver-linux64/chromedriver"
service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/129.0.2792.79")
driver = webdriver.Chrome(service=service, options=options)

numbers = '1234567890'
with open('naam.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        driver.get('https://www.instagram.com/accounts/emailsignup/')
        driver.implicitly_wait(10)
        
        # Filling the form
        enumber = ''.join(choices(numbers, k=5))
        email_input = driver.find_element(By.CSS_SELECTOR, "input[name='emailOrPhone']")
        email_input.send_keys(line + enumber + '@gmail.com')
        
        pnumber = ''.join(choices(numbers, k=7))
        password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password.send_keys(line + pnumber)
        
        fullname = driver.find_element(By.CSS_SELECTOR, "input[name='fullName']")
        fullname.send_keys(line)
        
        username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        unumber = ''.join(choices(numbers, k=5))
        username.send_keys(line + unumber)
        time.sleep(4)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'button'))
        )

        # Find all buttons
        buttons = driver.find_elements(By.TAG_NAME, 'button')

        # Print the HTML of each button
        for index, button in enumerate(buttons):
            print(f'Button {index + 1} HTML:')
            print(button.get_attribute('outerHTML'))

        # Click the second button (Sign up)
        if len(buttons) >= 2:
            sign_up_button = buttons[1]  # Index 1 for the second button
            if sign_up_button.is_enabled():  # Check if the button is enabled
                sign_up_button.click()  # Click the button
                print("Clicked on the Sign up button.")
            else:
                print("The Sign up button is disabled and cannot be clicked.")
        else:
            print("Less than two buttons found.")
        time.sleep(50)
        dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select[title='Month:']"))
        random_month_index = random.randint(0, 11)
        dropdown.select_by_index(random_month_index)
        dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select[title='Day:']"))
        random_day_index = random.randint(1, 30)
        dropdown.select_by_index(random_day_index)
        dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select[title='Year:']"))
        random_year_index = random.randint(0, len(dropdown.options) - 1)
        dropdown.select_by_index(random_year_index)
        button = driver.find_element(By.CSS_SELECTOR, "button._acan._acap._acaq._acas._aj1-._ap30")
        driver.execute_script("arguments[0].removeAttribute('disabled');", button)
        parent_div = driver.find_element(By.CSS_SELECTOR, "div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1sxyh0.xurb0ha.x1l90r2v.xyamay9.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1")
        driver.execute_script("arguments[0].style.display='none';", parent_div)
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(20)
        driver.find_element(By.CLASS_NAME, 'email_confirmation_code')
        button = driver.find_element(By.CSS_SELECTOR, "div[role='button'][tabindex='0'].x1i10hfl.xjqpnuy")
        time.sleep(100)
def login(email_user, email_pass):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_user, email_pass)
    mail.select("inbox")
    status, messages = mail.search(None, "ALL")
    mail_ids = messages[0].split()
    latest_email_id = mail_ids[-1]
    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")
            print("Title of the latest email:", subject)
            split_subject = subject.split('')
            print(split_subject[0])
