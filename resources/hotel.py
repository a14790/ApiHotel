from flask_restful import Resource, reqparse
from models.hotel import HotelModel
hoteis = [
    { "hotel_id": "paraiso", "nome": "Hotel Paraiso", "estrelas": 4.6, "diaria":123.99, "cidade": "Porto"},
    { "hotel_id": "fukui", "nome": "Fukui Resort", "estrelas": 4.8, "diaria":225.99, "cidade": "Viena"},
    { "hotel_id": "aguas", "nome": "Hotel Aguas", "estrelas": 4.2, "diaria":193.99, "cidade": "Lisboa"},
]
class Hoteis(Resource):
    def get(self):
        return { "hoteis": hoteis }
#Listar, inserir, atualizar, e eliminar um hotel especifico
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, help="Nome obrigatorio")
    argumentos.add_argument("estrelas", type=float, help="Estrelas obrigatorio")
    argumentos.add_argument("diaria", type=float, help="Diaria obrigatorio")
    argumentos.add_argument("cidade", type=str, help="Cidade obrigatorio")
    
    def get(self, id_hotel):
        for hotel in hoteis:
            if hotel["hotel_id"]== id_hotel:
                return hotel, 200
        return{ "message": "Hotel not found" }
    def post(self, id_hotel):
        dados = Hotel.argumentos.parse_args() # Dicionario
        for hotel in hoteis:
            if hotel["hotel_id"]== id_hotel:
                return{ "message": "Hotel with this id already exists" }, 404
        
        novo_hotel = HotelModel(id_hotel, **dados)
        
       # hoteis.append(novo_hotel) 
        return novo_hotel.json(), 200

    
    def put(self, id_hotel):
        dados = Hotel.argumentos.parse_args() # Dicionario
        for hotel in hoteis:
            if hotel["hotel_id"]== id_hotel:
                hotel_atualizado = { "hotel_id": id_hotel, **dados}
                hotel.update(novo_hotel)
                return hotel, 200
                
        novo_hotel ={"hotel_id": id_hotel, **dados }
        hoteis.append(novo_hotel)
        return novo_hotel; 201
    def delete(self, id_hotel):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel ["hotel_id"]!= id_hotel]
        return {"message": f"Hotel with {id_hotel} deleted"}