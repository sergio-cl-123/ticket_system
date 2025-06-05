from flask import Flask, redirect, url_for, render_template, request, flash
import mysql.connector
from flask_login import LoginManager, login_user, login_required, current_user
from config import config
#Models
from models.ModelUser import ModelUser
#Entities
from models.entities.User import User

app = Flask(__name__)
app.secret_key = 'mysecretkey'

# Configura Flask-Login
login_manager_app = LoginManager(app)
login_manager_app.login_view = 'Login'


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(Conectarse(0), id)


@app.route('/')
def index():
    return redirect(url_for('Login'))    

@app.route('/Login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        mydb = Conectarse(0)
        user = User(0, request.form['txtUser'], request.form['txtPass'], "", 0, 0)
        usuario_ok = ModelUser.login(mydb, user)
        if usuario_ok is not None:
            if usuario_ok.Pass:
                login_user(usuario_ok)
                return redirect(url_for('Main_Cotizaciones'))
            else:
                flash("Pass inválida")
        else:
            flash("Usuario no encontrado")
        return render_template('index.html')
    else:
        return render_template('index.html')
    

def Conectarse(sistema=0):

    #LOGIN
    if sistema == 0: 
        mydb2 = mysql.connector.connect(
                    # host = "localhost",
                    # user = "user_ext",
                    # password = "9!8z5WvPqXs5MBw",
                    # database = 'bd_ticket_lu')
                    
                    host = "sql10.freesqldatabase.com",
                    user = "sql10783172",
                    password = "MwGWc7RUmq",
                    database = 'sql10783172')
    #LOGIN
    # elif sistema==1:
    #      mydb = mysql.connector.connect(
    #                 host = "mysql-limiteurbano.alwaysdata.net",
    #                 user = "320313_lu",
    #                 password = "9!8z5WvPqXs5MBw",
    #                 database = 'limiteurbano_logindb')
    # #PEDIDOS -> Que es el mismo del chatbot
    # elif sistema==2:
    #      mydb = mysql.connector.connect(
    #                 host = "mysql-limiteurbano.alwaysdata.net",
    #                 user = "320313_lu",
    #                 password = "9!8z5WvPqXs5MBw",
    #                 database = 'limiteurbano_administraciondb')    
    return mydb2


@app.route('/mis_tickets')
@login_required
def Main_Cotizaciones():

    #VALIDO QUE EL USUARIO TENGA PERMISOS PARA ENTRAR AQUI
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    print(current_user.Tipo)
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    if current_user.Tipo != 1:
        return render_template('index.html')
    

    mydb = Conectarse(0)
    cursor = mydb.cursor()
    query = "SELECT idCotizacion, Fecha_Creacion, Fecha_Expiracion, Estado, Comunidad, Direccion, Comuna, Persona_Contacto, Celular, Email, Nombre_Archivo, Ruta_Archivo, Link_Descarga, Celular FROM cotizacion order by Estado, idCotizacion desc;"
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('mis_tickets.html', datos = data)


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()