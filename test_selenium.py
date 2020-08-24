from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import requests
from xml.etree import ElementTree
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from dateutil.relativedelta import relativedelta

url = 'https://contrataciondelestado.es/wps/poc?uri=deeplink%3Abusqueda_licitacion_vis&ubicacionOrganica=VWI4MQOJzFM%3D'
#Windows
browser = webdriver.Chrome('C:/Users/JM/Documents/chromedriver')

#pip install webdriver-manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install(), service_args=['--ignore-ssl-errors=true'])
browser.set_window_size(1120, 1120)
browser.implicitly_wait(10)
browser.get(url)

# Introduce contrato
contrato = browser.find_element_by_id('viewns_Z7_AVEQAI930OBRD02JPMTPG21004_:form1:text71ExpMAQ')
contrato.send_keys(browser.numExpediente)

