from .entities.User import User

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.cursor()
            sql = "select * from usuario where User='"+str(user.User)+"'"
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=User(row[0], row[1], User.check_password(row[2], user.Pass), row[3], row[4], row[5])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.cursor()
            sql = "select Id, User, Tipo, Nombre, Comunidad from usuario where Id="+str(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[3], row[2], row[4])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)