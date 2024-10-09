import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Настройка Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Инициализация драйвера
driver_path = "C:/IdeaProjects/AQA/chromedriver.exe"
driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

try:
    # Шаг 1: Открытие веб-сайта
    driver.get("https://ya.ru")
    # Шаг 2: Поиск по ключевому слову Selenium
    search_input = driver.find_element(By.NAME, "text")
    search_input.send_keys("Selenium")
    time.sleep(2)
    search_input.send_keys(Keys.RETURN)

    # Задержка для загрузки страницы
    time.sleep(2)

    # Шаг 3: Проверка результатов
    results = driver.find_elements(By.XPATH, "//li[contains(@class, 'serp-item')]")
    assert any("Selenium" in result.text for result in results), "Результаты поиска не содержат ключевое слово 'Selenium'"

    print("Тест пройден: ключевое слово 'Selenium' найдено в результатах поиска.")

except AssertionError as e:
    print(f"Ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()
