import sqlite3


def crear_base_de_datos_score():
    """Si no existe crea base de datos con y tabla con 3 columnas (id, nombre y score)"""
    with sqlite3.connect("base_de_datos_score") as conexion:
        try:
            sentencia = ''' create table scores
                            (
                            id integer primary key autoincrement,
                            nombre text,
                            score integer
                            )
                            '''
            conexion.execute(sentencia)
            print("Se creo la tabla de score")
        except sqlite3.OperationalError:
            print("La tabla score ya existe")

def agregar_score(nombre, score):
    """Agrega fila con nombre y score que se passen como prametros"""
    with sqlite3.connect("base_de_datos_score") as conexion:
        try:
            conexion.execute("insert into personajes(nombre, score)values (?,?)", (nombre, score))
            conexion.commit()
        except:
            print("Error 1")

def generar_top_5()->list:
    """Consulta bd y decuelve lista de top 5 score de mayor a menor"""
    with sqlite3.connect("base_de_datos_score") as conexion:
        try:
            consulta = "SELECT nombre, score FROM personajes ORDER BY score DESC LIMIT 5"
            lista = conexion.execute(consulta).fetchall()

            return lista  #retorma lista de tuplas

        except:
            print("Error 2")
            return None



    
    

