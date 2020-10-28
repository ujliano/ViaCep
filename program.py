#Importando bibliotecas externas
import requests
import json

#string do cep que quero pesquisar
cep = input("Por favor, digite um CEP válido: ")
#cep = '83502510'

#url da API que te mostrei do via cep + o cep que tá sendo digitado
#ali em cima
url_api = ('http://www.viacep.com.br/ws/%s/json' % cep)

#instancia um novo objeto request da biblioteca passando a url blabla
#mt encheção de linguiça, basicamente isso ai abre uma coñexão com a 
#internet e baixa o retorno, que é no caso o json do CEP
req = requests.get(url_api)

#aqui uma validação, se o status de internet retornar 200 a gente mostra
# os dados na tela, caso não nem mostra
#existe uma lista de web status, por exemplo
# 200 = OK
# 404 = conteudo não encontrado
# e por ai vai

if req.status_code == 200:
    #aqui eu faço a leitura do json que retorno, esse aqui  
    data = json.loads(req.text)
    #aqui eu encho mais liguiça passando pra outra variavel
    #da pra simplificar mais ainda o codigo
    objeto_texto  = data
    #aqui é importante, eu pego o campo 'cep' da variavel data
    #aqui é importante tbm , eu pego o campo 'logradouro' da variavel 
    # data que tava no json
    cepData = data['logradouro']
    cepBairro = data['bairro']
    cepEstado = data['uf']
    
    #aqui eu só printo
    #vou botar pra funcionar pra tu ver
    print("Endereço: " + cepData)
    print("Bairro: " + cepBairro)
    print("Estado: " + cepEstado)

else:
    print("Algo deu errado!")



