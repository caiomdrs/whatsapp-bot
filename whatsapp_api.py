from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class api:
    global driver

    driver = webdriver.Chrome()

    def login():
        driver.get("https://web.whatsapp.com")
        print("Scan QR Code, And then Enter")
        input()
        print("Logged In")


    def search_contact(contact: str):
        inp_xpath_search = "//div[@title='Caixa de texto de pesquisa']"
        input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
        input_box_search.click()
        time.sleep(2)
        input_box_search.send_keys(contact)
        time.sleep(2)


    def click_contact(contact: str):
        selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
        selected_contact.click()


    def send_message(message: str):
        inp_xpath = '//p[@class="selectable-text copyable-text iq0m558w"]'
        input_box = driver.find_element_by_xpath(inp_xpath)
        time.sleep(2)
        input_box.send_keys(message + Keys.ENTER)
        time.sleep(2)


    def get_messages():
        mes_xpath = '//span[@class="_11JPr selectable-text copyable-text"][@dir="ltr"]'
        msg_frm_xpath = '//div[@class="copyable-text"]'
        msg_frm_text = driver.find_elements_by_xpath(msg_frm_xpath)
        message_text = driver.find_elements_by_xpath(mes_xpath)
        time.sleep(2)
        for i in range(0, len(message_text)):
            message = str(message_text[i].text)
            message_from = str(msg_frm_text[i].get_attribute('data-pre-plain-text'))
            try:
                print(f"{message_from} {message}")
            except:
                pass
        time.sleep(2)