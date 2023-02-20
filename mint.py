import streamlit as st
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@st.experimental_singleton
def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
def run_session():
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    driver = get_driver()
    
    
    #driver = uc.Chrome(options=chrome_options)
    try:
        driver.get("https://mintme.onrender.com")
        print(f" connected to page")
        for i in range(0,10000000):
            print(i)
        
   
    except Exception as err:
       pass
    
while True:    
    run_session()
