# source: https://github.com/Ronald-TR/Buscando-distancia-por-cep-em-Python
#script has been tweaked for use case

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def distance(cep1, cep2):
    cep1 = str(cep1)
    cep2 = str(cep2)
    maps_key = os.getenv('MAPS_API_KEY')                                           #enjoy
    url1 = 'https://viacep.com.br/ws/' + cep1 + '/json/'
    url2 = 'https://viacep.com.br/ws/' + cep2 + '/json/'
    origem = json.loads(requests.get(url1).text)
    destino = json.loads(requests.get(url2).text)
    strOrigem = origem['logradouro'] + ' ' + origem['localidade'] + ' ' + origem['uf']
    strOrigem = strOrigem.replace(' ', '+')
    strDestino = destino['logradouro'] + ' ' + origem['localidade'] + ' ' + origem['uf']
    strDestino = strDestino.replace(' ', '+')
    google_data = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins='
                     +strOrigem+'&destinations='+strDestino+'&key='+maps_key)    #adicione o campo &key= ao final, com a sua chave de api distancematrix,
                                                                #obtida gratuitamente no seu site oficial caso use fora do ambiente de testes
    
    parsed_google_data = json.loads(google_data.text)
    parsed_distance = parsed_google_data['rows'][0]['elements'][0]['distance']['text']

    return parsed_distance                                                           
                                                                
#Exemplo de chamada
# resultado = rota('88050001', '88056300')
# print(resultado)