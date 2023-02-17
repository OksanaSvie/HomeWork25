# Домашнее задание 25
# На основании того, что проходили на паре по Selenium WebDriver,
# написать программу которая заходит на выбранный заранее сайт,
# нажимает на различные элементы меню данного сайта,
# с переходом на дополнительные страницы
# и делает снимки экрана данных страниц (не менее 10 разных страниц).
# Прислать проект в .zip архиве.

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://www.leman.in.ua/'

driver.get(url)


xpath_1 = '//img[@title="CHRISTMAS SALE"]'
button_1 = driver.find_element('xpath', xpath_1)
button_1.click()
driver.get_screenshot_as_file('first.png')

xpath_2 = '//a[@href="https://www.leman.in.ua/" and @class="header__logo"]'
button_2 = driver.find_element('xpath', xpath_2)
button_2.click()
driver.get_screenshot_as_file('second.png')

xpath_3 = '//img[@title="Светри і гольфи"]'
button_3 = driver.find_element('xpath', xpath_3)
button_3.click()
driver.get_screenshot_as_file('third.png')

xpath_4 = '//a[@href="https://www.leman.in.ua/odezhda/svitera-i-golfy/golf-bazovii-chernii-odnotonnii-leman-lm4527-3.html" and @tabindex="0"]' #golf
button_4 = driver.find_element('xpath', xpath_4)
button_4.click()
driver.get_screenshot_as_file('fourth.png')

xpath_5 = '//img[@title="Гольф базовий однотонний білий LEMAN LM4527-2"]'
button_5 = driver.find_element('xpath', xpath_5)
button_5.click()
driver.get_screenshot_as_file('fifth.png')

xpath_6 = '//img[@title="Гольф базовий однотонний білий LEMAN LM4527-2" and @src="https://www.leman.in.ua/image/cache/catalog/odezhda/golfy/lm4527/img_7030-auto_width_70.jpg.webp" ]'# vtorii bilij golf
button_6 = driver.find_element('xpath', xpath_6)
button_6.click()
driver.get_screenshot_as_file('sixth.png')

xpath_7 = '//a[@href="https://www.leman.in.ua/" and @class="header__logo"]'
button_7 = driver.find_element('xpath', xpath_7)
button_7.click()
driver.get_screenshot_as_file('seventh.png')

xpath_8 = '//a[@href="https://www.leman.in.ua/new-year-collection/"]'
button_8 = driver.find_element('xpath', xpath_8)
button_8.click()
driver.get_screenshot_as_file('eighth.png')

xpath_9 = '//a[@href="https://www.leman.in.ua/about_us.html"]'
button_9 = driver.find_element('xpath', xpath_9)
button_9.click()
driver.get_screenshot_as_file('ninth.png')

xpath_10 = '//a[@href="https://www.leman.in.ua/contact-us/" and @class="nav-top__link"]'
button_10 = driver.find_element('xpath', xpath_10)
button_10.click()
driver.get_screenshot_as_file('tenth.png')

time.sleep(5)