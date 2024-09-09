from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_website(url):
    # Setup Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    service = Service(executable_path='/path/to/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        
        # Example: Wait for AI-generated content to load, if necessary
        # You can use WebDriverWait to wait for specific elements
        # Example: WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'ai-response')))

        # Get the page source and parse it with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Scrape the AI-generated content
        titles = [title.get_text() for title in soup.find_all('h2', class_='article-title')]
        
        return {
            "status": "success",
            "data": titles
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
    finally:
        driver.quit()  # Close the browser session
