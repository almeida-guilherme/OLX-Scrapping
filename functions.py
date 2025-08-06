from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import os
from time import sleep

def getNavigationList(driver):
  #Essa etapa do código serve para ver o navegador
  navigation_buttons = driver.find_elements(By.CSS_SELECTOR,"#listing-pagination > aside > div > button")
  navigation_aside_list_div_buttons_a = []

  for Currentbutton in navigation_buttons:
    navigation_aside_list_div_buttons_a.append(Currentbutton.find_element(By.TAG_NAME,"a").get_attribute("href"))
  currentIndexPage = len(navigation_buttons) - 3

  return currentIndexPage,list(set(navigation_aside_list_div_buttons_a))

def getAllLinksList(driver,links_allElements):
  links_list = driver.find_elements(By.CLASS_NAME,"olx-adcard__link")
  for element in links_list:
    links_allElements.append(element.get_attribute("href"))
  return list(set(links_allElements))

def navigateBetweenThePages(navigationList,driver):
  links_allElements = []
  #Verifique a quantidade de paginas
  for currentNavigation in navigationList:
    driver.set_page_load_timeout(60)  # ou um valor maior, se necessário
    try:
      driver.get(currentNavigation)
    except:
      print("Error ao acessar o drive atual")
      # Setando os valores do driver
      #Inicializa o navegador
      driver.quit()
      options = uc.ChromeOptions()
      options.add_argument("start-maximized")
      chrome_profile_dir =  os.path.abspath('./chrome_profile_1')
      options.add_argument(f'--user-data-dir={chrome_profile_dir}/')
      service = Service(executable_path=".\chromedriver.exe")
      driver = uc.Chrome(options=options)
      driver.get(currentNavigation)
    sleep(2)
    currentLinksList = getAllLinksList(driver,links_allElements)
    links_allElements = list(dict.fromkeys(links_allElements+currentLinksList))
    
  return list(set(links_allElements)),driver
def sendMessageToUser(driver,message,productName):
  description_title_span = driver.find_element(By.CSS_SELECTOR, "#description-title > div > div > span").text
  if productName.upper() in description_title_span.upper():
    chat_button = driver.find_element(By.ID,"price-box-button-chat")
    chat_button.click()
    sleep(3)
    try:
      elemento = driver.find_element(By.XPATH, '//*[@id="mercurie-remote"]/div/div/div/div[3]/div/div/span')
      return print("Usuario atual bloqueado")
    except:

        print("Usuario atual não bloqueado")

    WebDriverWait(driver,10).until(
      EC.presence_of_element_located((By.ID,"input-text-message"))
    )
    chat_input = driver.find_element(By.ID,"input-text-message")
    chat_input.send_keys(message+Keys.ENTER)