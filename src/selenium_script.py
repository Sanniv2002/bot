# selenium_script.py

from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def audio_stream_bot():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    #chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the local server page
        driver.get("http://localhost:8000/index.html")
        
        # Pause the script to inspect the browser
        input("Press Enter to close the browser...")
    finally:
        pass
        driver.quit()  # Close the browser properly


audio_stream_bot()