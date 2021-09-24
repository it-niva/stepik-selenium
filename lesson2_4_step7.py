from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x): 
        return str(math.log(abs(12*math.sin(int(x)))))
try:
        link = "https://suninjuly.github.io/explicit_wait2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        #time.sleep(1)
        #browser.execute_script("window.scrollBy(0, 150);")
        #browser.execute_script('return arguments[0].scrollIntoView(true);',)
        #option1 = browser.find_element_by_id("robotCheckbox").click()
        #option2 = browser.find_element_by_id("robotsRule").click()
        #browser.find_element_by_css_selector("button.btn").click()
        #first_window = browser.window_handles[0]
        #new_window = browser.window_handles[1]
        #browser.switch_to.window(new_window)
        #browser.switch_to.alert.accept()
        option1 = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price",),"$100"))
        option2 = browser.find_element_by_id("book").click()
        option3 = browser.find_element_by_id("input_value")
        x = option3.text
        y = calc(x)
        print(x)
        option4 = browser.find_element_by_id("answer").send_keys(y)
        option5 = browser.find_element_by_id("solve").click()
    # Ваш код, который заполняет обязательные поля
    #first_name = browser.find_element_by_css_selector('[class="first_block"] [class="form-control first"]').send_keys('123')

    #first_name = browser.find_element_by_css_selector('[class="first_block"] [class="form-control second"]').send_keys('123')

    #first_name = browser.find_element_by_css_selector('[class="first_block"] [class="form-control third"]').send_keys('123')

    # Отправляем заполненную форму
    #button = browser.find_element_by_css_selector("button.btn")
    #button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    
    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(35)
    # закрываем браузер после всех манипуляций
    browser.quit()
