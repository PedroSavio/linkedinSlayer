import scrapy

import scrapy

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


class LinkdinSlayer:

    def __init__(self, linkdin_email, linkdin_password, number_pages, job_search, only_easy_apply, only_remote):
        self.linkdin_email = linkdin_email
        self.linkdin_password = linkdin_password
        self.number_pages = number_pages
        self.job_search = job_search
        self.only_easy_apply = only_easy_apply
        self.only_remote = only_remote

    def start_requests(self):
        print("Tela de Login")
        chrome_options = ChromeOptions()

        driver = Chrome(options=chrome_options)

        driver.get('https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username")))

        email = driver.find_element(By.ID, "username")
        email.send_keys(self.linkdin_email)
        sleep(2)
        password = driver.find_element(By.ID, "password")
        password.send_keys(self.linkdin_password)
        sleep(1)

        btn_logar = driver.find_element(By.CSS_SELECTOR, ".btn__primary--large")
        btn_logar.click()

        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//nav[@aria-label='Navegação principal']/ul/li[3]")))
        sleep(5)

        btn_vagas = driver.find_element(By.XPATH, "//nav[@aria-label='Navegação principal']/ul/li[3]")
        btn_vagas.click()

        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@aria-label='Pesquisar cargo, competência ou empresa']")))
        sleep(1)

        input_vagas = driver.find_element(By.XPATH,
                                          "//input[@aria-label='Pesquisar cargo, competência ou empresa']")
        input_vagas.send_keys(self.job_search)

        vagas = driver.find_elements(By.XPATH, "//div[@class='jobs-search-results-list']/ul/li")

        for vaga in vagas:
            vaga.click()
            sleep(2)
            label_btn_candidatar = driver.find_element(By.XPATH, "//button[@class='jobs-apply-button artdeco-button artdeco-button--icon-right artdeco-button--3 artdeco-button--primary ember-view']/span")
            if label_btn_candidatar.text == "Aplicar":
                label_btn_salvar = driver.find_element(By.XPATH, "//button[@class='jobs-save-button artdeco-button artdeco-button--3 artdeco-button--secondary']/span")
                label_btn_salvar.click()
            elif label_btn_candidatar.text == "Candidatura simplificada":
                label_btn_candidatar.click()
                sleep(2)
                btn_avancar = driver.find_element(By.XPATH, "//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
                btn_avancar.click()
                continue