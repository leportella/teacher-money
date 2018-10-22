import requests
from bs4 import BeautifulSoup as bs

servidor = 3617364

url = 'http://www.portaltransparencia.gov.br/servidores/{}'.format(servidor)

response = requests.get(url)

soup = bs(response.content
div = soup.find('div', {'id': 'box-remuneracao'})

navegador = soup.find('ul', {'class': 'nav-tabs--box-grafico'})
items_navegador = navegador.findAll('li')

meses = []
for item in items_navegador:
    meses.append([item.text, item.a.attrs['aria-controls']])


mes1 = meses[0]
div_mes1 = soup.find('div', {'id': mes1[1]})

remuneracao_titulo = div_mes1.find('span',
                                   text='Remuneração básica bruta:')

salario_bruto = remuneracao_titulo.findNext().text

red_spans = div_mes1.findAll('span', {'class': 'red'})
descontos = [span.text for span in red_spans if span.text[0] == '-']
