import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',      # Dirección del servidor de MySQL
            user='root',           # Nombre de usuario, normalmente root
            password='Tupassword', # Contraseña de la cuenta que utilizamos
            database='semana8'     # Nombre de la base de datos a la cual nos conectaremos
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Ejemplo de uso
conn = connect_to_database()
if conn:
    conn.close()

#ultimo cambio realizado