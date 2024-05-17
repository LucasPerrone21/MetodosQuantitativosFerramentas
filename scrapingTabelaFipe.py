from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from salvaExcel import salvaExcel





chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico, options=chrome_options)

navegador.get('https://veiculos.fipe.org.br/')

#passo a passo pra selecionar a marca

time.sleep(2)
init = navegador.find_element('xpath', "//*[@id='front']/div[1]/div[1]/ul/li[1]/a")
time.sleep(1)
init.click()

#passo a passo pra selecionar os modelos

contadorModelo = 0
contadorAno = 0


navegador.find_element(By.XPATH, value='//*[@id="selectMarcacarro"]')

navegador.find_element(By.XPATH, value='//*[@id="selectMarcacarro"]/option[8]').click()
navegador.find_element(By.XPATH, value='//*[@id="selectAnoModelocarro"]').click()
modelos = navegador.find_elements(By.XPATH, value='//*[@id="selectAnoModelocarro"]/option')
modelos.pop(0)
qtdModelos = len(modelos)

time.sleep(3)



for modelosNum in range(qtdModelos):
    navegador.find_element(By.XPATH, value='//*[@id="selectMarcacarro"]').click()
    navegador.find_element(By.XPATH, value='//*[@id="selectMarcacarro"]/option[8]').click()
    navegador.find_element(By.XPATH, value='//*[@id="selectAnoModelocarro"]').click()
    modelos = navegador.find_elements(By.XPATH, value='//*[@id="selectAnoModelocarro"]/option')
    modelos.pop(0)
    carro = modelos[contadorModelo]
    carro.click()
    contadorModelo += 1

    anos = navegador.find_elements(By.XPATH, value='//*[@id="selectAnocarro"]/option')
    anos.pop(0)
    qtdAnos = len(anos)
    carro.click()
    print(qtdAnos, "passei daqui")


    for anosNum in range(qtdAnos):
        anos = navegador.find_elements(By.XPATH, value='//*[@id="selectAnocarro"]/option')
        anos.pop(0)
        ano = anos[anosNum]
        ano.click()

        navegador.find_element(By.XPATH, value='//*[@id="buttonPesquisarcarro"]').click()
        time.sleep(1)
        marca = navegador.find_element(By.XPATH, value='//*[@id="resultadoConsultacarroFiltros"]/table/tbody/tr[3]/td[2]/p').text
        modelo = navegador.find_element(By.XPATH, value='//*[@id="resultadoConsultacarroFiltros"]/table/tbody/tr[4]/td[2]/p').text
        ano = navegador.find_element(By.XPATH, value='//*[@id="resultadoConsultacarroFiltros"]/table/tbody/tr[5]/td[2]/p').text
        valor = navegador.find_element(By.XPATH, value='//*[@id="resultadoConsultacarroFiltros"]/table/tbody/tr[8]/td[2]/p').text

        dados = {
            'Marca': [marca],
            'Modelo': [modelo],
            'Ano': [ano],
            'Valor': [valor]
        }

        salvaExcel(dados)

        time.sleep(.5)
    
    navegador.find_element(By.XPATH, value='//*[@id="buttonLimparPesquisarcarro"]/a').click()


