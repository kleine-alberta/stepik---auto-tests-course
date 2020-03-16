from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome() 
    browser.get(link)            
 
    def calc(sum):
    	return str(int(x) + int(y))
    

    x_element = browser.find_element_by_css_selector("#num1")
    y_element = browser.find_element_by_css_selector("#num2")

    x = x_element.text
    y = y_element.text
    z = calc(sum)
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z) # ищем элемент 
  


    #submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()