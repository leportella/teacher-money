import json
import requests

numero = 3500
url = f'http://www.portaltransparencia.gov.br/servidores/consulta/resultado?paginacaoSimples=false&tamanhoPagina={numero}&offset=0&direcaoOrdenacao=asc&colunaOrdenacao=nome&colunasSelecionadas=detalhar,tipo,situacao,cpf,nome,orgaoSuperiorLotacao,orgaoLotacao,orgaoSuperiorExercicio,orgaoExercicio,orgaoSuperiorServidorLotacao,orgaoServidorLotacao,orgaoSuperiorServidorExercicio,orgaoServidorExercicio,matricula,tipoVinculo,funcao,licenca&orgaosExercicio=OR26435&_=1540214854813'

response = requests.get(url)
content = json.loads(response.content)
servidores = content['data']

print('status', response.status_code)
print('numero de servidores', len(servidores))

with open('servidores_ifrn.json', 'w') as outfile:
    json.dump(content['data'], outfile)
