from flask_restful import Resource, reqparse

hoteis = [
    {"hotel_id": "paraiso", "nome": "Hotel Paraiso", "estrelas": 4.6, "diaria": 123.99, "cidade": "Porto"},
    {"hotel_id": "fukui", "nome": "Hotel Resort", "estrelas": 4.8, "diaria": 255.99, "cidade": "Viena"},
    {"hotel_id": "agua", "nome": "Hotel Aguas", "estrelas": 4.2, "diaria": 193.99, "cidade": "Lisboa"},
]

# Listar todos os hotéis
class Hoteis(Resource):
    def get(self):
        return {"hoteis": hoteis}


# Listar, inserir, atualizar e eleminar um hotel especifico
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, help="Nome Obrigatorio")
    argumentos.add_argument("estrelas", type=float, help="Estrelas Obrigatorio")
    argumentos.add_argument("diaria", type=float, help="Diaria Obrigatorio")
    argumentos.add_argument("cidade", type=str, help="Cidade Obrigatorio")
    def get(self, id_hotel):
        for hotel in hoteis:
            if hotel["hotel_id"] == id_hotel:
                return hotel, 200

        return {"message": "Hotel Not found"}, 404

    def post(self, id_hotel):
        for hotel in hoteis:
            if hotel["hotel_id"] == id_hotel:
                return hotel, 200 
            return {"message": "Hotel not found"}

    def post(self, id_hotel):
        dados = Hotel.argumentos.parse_args()
        for hotel in hoteis:
            if hotel["hotel_id"] == id_hotel:
                return {"message": "Hotel with this id already exists"}
        novo_hotel = {"hotel_id": id_hotel,**dados}
        hoteis.append(novo_hotel)
        return novo_hotel, 200