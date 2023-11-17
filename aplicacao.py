#Construir a API com Flask
from flask import Flask, request
import joblib



#Instanciar o aplicativo
Aplicativo =  Flask(__name__)

#Carregar o modelo
Modelo = joblib.load('Modelo_Floresta_Aleatorio_v100.pkl')


#Função para receber  nossa API
@Aplicativo.route('/API_Preditivo/<area>;<rooms>;<bathroom>;<parking_spaces>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>', methods=['GET'])

#	area	rooms	bathroom	parking spaces	floor	animal	furniture	hoa (R$)	property tax (R$)

def Funcao01(area, rooms, bathroom, floor, parking_spaces, animal, furniture, hoa, property_tax):

    #Recebndo os inputs da API
    Lista = [float(area), float(rooms), float(bathroom), float(parking_spaces), float(floor), float(animal), float(furniture), float(hoa), float(property_tax)]

    try:

        #Fazer previsão
        Previsao = Modelo.predict( [Lista] )

        #retorno do Modelo
        return {'Valor_Aluguel' : str(Previsao)}
    
    except:
        return{'Aviso':'Deu algum erro!'}


if __name__ == '__main__':
    Aplicativo.run(debug=True)

#Jupyter conexão ---> Flask