import requests
import re

def get_h3_headings(url):
    try:
        # Получаем содержимое веб-страницы
        response = requests.get(url)
        if response.status_code == 200:
            # Используем регулярное выражение для поиска подзаголовков в тегах <h3>
            headings = re.findall(r'<h3.*?>(.*?)</h3>', response.text)
            return headings
        else:
            print("Ошибка при получении страницы. Код состояния:", response.status_code)
            return None
    except requests.RequestException as e:
        print("Ошибка запроса:", e)
        return None

# URL веб-страницы для проверки
url = 'http://www.columbia.edu/~fdc/sample.html'

# Получаем список подзаголовков
headings_list = get_h3_headings(url)

if headings_list:
    print(headings_list)
