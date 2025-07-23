# todo-selenium-automation

Automation script for a Todo web app using **Python** and **Selenium**.

---

## 📦 Tools Used

- **Python 3** – programming language used to write the script  
- **Selenium WebDriver** – browser automation framework  
- **Google Chrome** – the browser being automated  
- **ChromeDriver** – acts as a bridge between Selenium and Chrome

## 📝 Assumptions Made
- ChromeDriver is compatible with the installed Chrome version
- Script is run on Windows (adjust paths accordingly for macOS/Linux)
- Internet connection is available to load the TodoMVC app
- No login/authentication is required in the tested app

## ✅ What the Script Does
- Opens the TodoMVC app
- Adds a new task: "Buy Milk"
- Marks the task as complete
- Deletes the task
- Closes the browser
---

## ▶️ How to Run the Automation Script

1. Install Selenium

pip install selenium

2. Install ChromeDriver

Download the version that matches your browser from:
https://chromedriver.chromium.org/downloads

Extract the downloaded file and place the chromedriver.exe in a known directory (e.g., C:/webdrivers/)

3. Set Up Your Script:

Ensure that your script includes the correct path to your chromedriver. 

Here's an example setup from todo_test.py

from selenium import webdriver  

from selenium.webdriver.chrome.service import Service  

from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  

chrome_options.add_argument("--start-maximized")  

Update path for your system:

service = Service("C:/path/to/chromedriver.exe")  

driver = webdriver.Chrome(service=service, options=chrome_options)

4. Update Element Selectors (if needed)

If the HTML structure of the Todo app changes, you may need to update class selectors (names, tags, or XPaths) in the script.

5. Run the Script
To execute your automation:

python todo_test.py
