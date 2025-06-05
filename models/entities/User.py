from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, Id, User, Pass, Nombre, Tipo, Comunidad):
        self.Id = Id
        self.User = User
        self.Pass = Pass
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Comunidad = Comunidad

    def get_id(self):
        return str(self.Id)
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)