from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
import pyautogui
driver = webdriver.Chrome(options=options)
window = pyautogui.getWindowsWithTitle(pyautogui.getActiveWindowTitle())[0]
window.minimize()
query_string = input("Query string: ")
url = f"https://www.perplexity.ai/search?q=hello&focus=internet"
driver.get(url)
wait = WebDriverWait(driver, 40)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fa-circle-plus")))
parent_element = driver.find_element(By.CSS_SELECTOR, ".fa-circle-plus").find_element(By.XPATH, "..")
main = parent_element.find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..")
textarea = main.find_element(By.TAG_NAME, "textarea")
textarea.send_keys("Some text to input")
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".dark\\:prose-invert")))
elements = driver.find_elements(By.CSS_SELECTOR, ".dark\\:prose-invert")
with open("results.txt", "w") as results:
    results.write(elements[0].text)