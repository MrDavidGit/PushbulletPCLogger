from pushbullet import Pushbullet
from dotenv import load_dotenv
import os
from datetime import datetime
import psutil
import mariadb

load_dotenv()

pb = Pushbullet(os.getenv("API_KEY"))

# Datos de conexión a MariaDB
DB_HOST = "localhost"         # Cambia por tu host
DB_PORT = 3306                # Cambia si usas un puerto diferente
DB_USER = "root"              # Cambia por tu usuario
DB_PASSWORD = "password"      # Cambia por tu contraseña
DB_NAME = "mi_base_de_datos"  # Cambia por el nombre de tu base de datos

# Obtener la hora actual
fecha_inicio = datetime.now()

# Obtener la hora exacta de arranque del sistema
hora_arranque = datetime.fromtimestamp(psutil.boot_time())

# Diferencia de tiempo entre ahora y el arranque del sistema (en segundos redondeados)
tiempo_arranque = round((datetime.now() - hora_arranque).total_seconds(), 2)

# Fecha en formato YYYY-MM-DD (compatible con MariaDB)
fecha_inicio_formateada = fecha_inicio.strftime('%Y-%m-%d')

# Formato de hora
hora_inicio = fecha_inicio.strftime('%H:%M:%S')

# Conexión a la base de datos
conn = mariadb.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""CREATE TABLE IF NOT EXISTS INICIO (
               id INT PRIMARY KEY AUTO_INCREMENT,
               hora TIME NOT NULL,
               tiempo_arranque FLOAT NOT NULL,
               fecha DATE NOT NULL
            )
            """)

# Insertar datos
cursor.execute("""
               INSERT INTO INICIO (hora, tiempo_arranque, fecha)
               VALUES (?, ?, ?)
                """, (hora_inicio, tiempo_arranque, fecha_inicio_formateada))
conn.commit()

# Envio de notificación por Pushbullet
Titulo = "Inicio del dispositivo"
Descripcion = f"El dispositivo se ha iniciado a las {hora_inicio} tardando {tiempo_arranque}s en arrancar."

pb.push_note(Titulo, Descripcion)

# Cerrar conexión a la base de datos
cursor.close()
conn.close()