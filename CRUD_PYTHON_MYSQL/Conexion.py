import mysql.connector

class CConexxion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user = "", 
                                            password = "", 
                                            host = "", 
                                            database = "", 
                                            port = "")
            
        except mysql.connector.Error as error:
            print("Error al conectarte a la base de datos {}".format(error))