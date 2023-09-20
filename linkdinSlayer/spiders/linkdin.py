import scrapy

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


class LinkdinSpider(scrapy.Spider):
    name = "linkdin"

    def start_requests(self):
        print("Iniciando spyder linkdin")
        yield scrapy.Request("https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin", callback=self.login)

    def parse(self, response):
        print("Tela de Login")
        chrome_options = ChromeOptions()

        if not self.settings.get('DEV_MODE'):
            chrome_options.add_argument("--headless")

        driver = Chrome(options=chrome_options)

        driver.get(response.url)
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username")))

        email = driver.find_element(By.ID, "username")
        email.send_keys(self.settings.get("EMAIL_LINKDIN"))
        sleep(2)
        password = driver.find_element(By.ID, "password")
        password.send_keys(self.settings.get("PASSWORD_LINKDIN"))
        sleep(2)

        driver.find_element(By.CSS_SELECTOR, ".btn__primary--large").click()

        btn_vagas = driver.find_element(By.XPATH, "//nav[@aria-label='Navegação principal']/ul/li[3]")
        btn_vagas.click()
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Pesquisar cargo, competência ou empresa']")))
        sleep(1)

        input_vagas = driver.find_element(By.XPATH, "//input[@aria-label='Pesquisar cargo, competência ou empresa']")
        input_vagas.send_keys(s)

        vagas = driver.find_elements(By.XPATH, "//div[@class='jobs-search-results-list']/ul/li")



