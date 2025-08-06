from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import json
import functions
import os
from pathlib import Path
from selenium.webdriver.common.by import By
from time import sleep

# Leia o arquivo Json
with open('data.json', 'r',encoding='utf-8') as file:
    dataJson = json.load(file)

# Atribua os valores do Json em variaveis
dataAdList = list(dict.fromkeys(dataJson.get("ad_List")))
allProducts = list(dataJson.get("products"))
message = dataJson.get("message")

#Inicializa o navegador
options = uc.ChromeOptions()
options.add_argument("start-maximized")

#Crie um perfil para ficar salvo os cookies
chrome_profile_dir =  os.path.abspath('./chrome_profile_1')

# Caso não exista o perfil
if not os.path.isdir(chrome_profile_dir):
    os.mkdir(chrome_profile_dir)
Path(f'{chrome_profile_dir}/First Run').touch()

# Setando os valores do driver
options.add_argument(f'--user-data-dir={chrome_profile_dir}/')
service = Service(executable_path=".\chromedriver.exe")
driver = uc.Chrome(options=options)

'''Código principal. Aqui estamos percorrendo por todos os produtos do "All Products"
   Cada produto possui uma URL e possui o nome do produto. Iremos usar o nome do produto para verificar se estamos buscando o produto certo
'''
for currentProduct in allProducts:
  #Pegando o valor da url e do nome do produto
  productName = ""
  productURL = ""
  for currentKey,currentValue in currentProduct.items():
    productName = currentKey
    productURL = currentValue
  
  
  #Acessando a pagina do produto
  driver.get(productURL)

  #Essa lista servira para armazenar todos os links buscados na sessão atual
  links_allElements = []


  #Aqui estamos pegando o valor e a quantidade de todos os indices das paginas 
  currentIndexPage,navigationList = functions.getNavigationList(driver)
  if (currentIndexPage == 1):

    #Caso tenhamos apenas uma página, pegue diretamente todos os links
    links_allElements = functions.getAllLinksList(driver,links_allElements)
  else:
    
    #Caso tenhamos mais de uma pagina, transcorra por todas as paginas
    links_allElements,driver = functions.navigateBetweenThePages(navigationList,driver)

  if len(dataAdList) == 0:
    #Caso seja a primeira vez que esse produto está sendo executado, ele não havera nem um produto registrado
    dataJson["ad_List"] = links_allElements
  else:
    #Aqui temos certeza que já executamos alguma vez esse produto
    for element in dataAdList:  
      if element in links_allElements:
        links_allElements.remove(element)
        #Pegue apenas os anuncios que nunca foram acessados

    if len(links_allElements) == 0:
      #Caso todos os anuncios já foram acessados, feche o programa
      exit()
    else:
      #Adicione os links atuais para o arquivo json
      dataJson["ad_List"] = list(dict.fromkeys(dataAdList+links_allElements))

  for currentLink in links_allElements:
    try:
      #Aqui iremos acessar cada produto e enviar mensagem para o usuario
      driver.get(currentLink)
      functions.sendMessageToUser(driver,message,productName)
    except:
      print("There is a error in the link: "+ currentLink)
      continue   
    
  #Salve o Json
  with open('data.json', 'w') as file:
      json.dump(dataJson, file)