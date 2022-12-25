from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings
import time


def web_manipulator():
    driver = webdriver.Chrome()
    driver.get('https://web.telegram.org')
    wait = WebDriverWait(driver, timeout=4)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, settings.libpn_xpath_first)))
        log_in_switch_butt = driver.find_element(By.XPATH, settings.libpn_xpath_first)
    except Exception:
        wait.until(EC.visibility_of_element_located((By.XPATH, settings.libpn_xpath_second)))
        log_in_switch_butt = driver.find_element(By.XPATH, settings.libpn_xpath_second)
    log_in_switch_butt.click()
    try:
        wait.until(EC.visibility_of_element_located((By.ID, settings.phone_input_id)))
        phone_input = driver.find_element(By.ID, settings.phone_input_id)
    except Exception:
        wait.until(EC.visibility_of_element_located((By.XPATH, settings.phone_input_xpath)))
        phone_input = driver.find_element(By.XPATH, settings.phone_input_xpath)
    phone_input.send_keys(settings.phone_number)
    try:
        driver.find_element(By.XPATH, settings.next_button_xpath_first).click()
    except Exception:
        driver.find_element(By.XPATH, settings.next_button_xpath_second).click()
    time.sleep(40)



if __name__ == '__main__':
    web_manipulator()
