
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc

def run_session():
    chrome_options = uc.ChromeOptions()
    chrome_options.headless = True 
    chrome_options.add_argument("--no-sandbox")
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = uc.Chrome(options=chrome_options)
    try:
        driver.get("https://mrscan.onrender.com")
        print(f" connected to page")
        for i in range(0,10000000):
            print(i)
        
   
    except Exception as err:
       pass
    
while True:    
    run_session()
