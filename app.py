from flask_restful import Resource, reqparse
from models.user import UserModel
from hmac import compare_digest
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from blocklist import BLOCKLIST


class User(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, help="Nome obrigatorio")
    argumentos.add_argument("estrelas", type=float, help="Estrelas obrigatorio")
    argumentos.add_argument("diaria", type=float, help="Diaria obrigatorio")
    argumentos.add_argument("cidade", type=str, help="Cidade obrigatorio")
    
    def get(self, username):
       user_encontrado = UserModel.find_user(username)
       if user_encontrado:
            return user_encontrado.json(), 200
       return{ "message": "user not found" }


    @jwt_required()
    def delete(self, username):
        user_econtrado = UserModel.find_user(username)
        if user_econtrado:
            user_econtrado.delete_hotel()
            return {"message": f"Hotel with {username} deleted"}, 200
        return {"message": "User not found"}, 404




class UserRegister(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("username", type=str, help="Username obrigatorio")
    argumentos.add_argument("password", type=str, help="Password obrigatorio")
    




    def post(self):
        dados = UserRegister.argumentos.parse_args() # Dicionario
        user_encontrado = UserModel.find_user(dados["username"])
        if user_encontrado:
            return {"message": "User with this username already exists" }, 404
        novo_user = UserModel(**dados)
        novo_user.save_user()
        return novo_user.json(), 200
    
class UserLogin(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("username", type=str, help="Username obrigatorio")
    argumentos.add_argument("password", type=str, help="Password obrigatorio")


    def post(self):
        dados = UserLogin.argumentos.parse_args()
        user = UserModel.find_user(dados["username"])


        if user and compare_digest(user.password,dados["password"]):
            token = create_access_token(identity=user.username)
            return {"acess_token": token }
        return{"message": "Username or password invalid"}, 401


class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()["jti"]
        BLOCKLIST.add(jwt_id)
        return {"message": "User logged out successfuly"}