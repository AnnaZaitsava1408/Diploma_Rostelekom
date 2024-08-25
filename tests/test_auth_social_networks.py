import time
from selenium.webdriver.common.by import By


# python -m pytest -v --driver Chrome --driver-path C:\chromedriver\chromedriver.exe tests/test_auth_social_networks.py

# ТЕСТ № 1
def test_vk_page(driver):
    """Авторизация через VK"""
    driver.find_element(By.XPATH, '//*[@id="oidc_vk"]').click()
    time.sleep(4)

    assert driver.find_element(By.XPATH,
                               '//*[@id="root"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]')  # Проверяем переход по ссылке на быстрый вход в vk по  qr-коду


# ТЕСТ № 2
def test_mail_page(driver):
    """Авторизация через Mail"""
    driver.find_element(By.XPATH, '//*[@id="oidc_mail"]').click()
    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="wrp"]')


# ТЕСТ № 3
def test_Tinkoff_page(driver):
    """Авторизация через Тиньков"""
    driver.find_element(By.XPATH, '//*[@id="oidc_tinkoff"]').click()
    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="form-title"]')


# ТЕСТ № 4
def test_OK_page(driver):
    """Авторизация через Одноклассники"""
    driver.find_element(By.XPATH, '//*[@id="oidc_ok"]').click()
    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="widget-el"]/div[2]')
