from pushbullet import Pushbullet
from dotenv import load_dotenv
import os
from datetime import datetime
import mariadb
import socket

# Cargar las variables de entorno
load_dotenv()

# Configuración de Pushbullet
pb = Pushbullet(os.getenv("API_KEY"))

# Obtener la hora actual
fecha_inicio = datetime.now()

# Fecha en formato YYYY-MM-DD (Compatible con MariaDB)
fecha_formateada = fecha_inicio.strftime('%Y-%m-%d')

# Formato de hora
hora_formateada = fecha_inicio.strftime('%H:%M:%S')

# Obtener el nombre del equipo
nombre_equipo = socket.gethostname()

# Conexión a la base de datos
conn = mariadb.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""CREATE TABLE IF NOT EXISTS INICIO (
               id INT PRIMARY KEY AUTO_INCREMENT,
               nombre_equipo VARCHAR(255) NOT NULL,
               hora TIME NOT NULL,
               fecha DATE NOT NULL
            )
            """)

# Insertar datos
cursor.execute("""
               INSERT INTO INICIO (nombre_equipo, hora, fecha)
               VALUES (?, ?, ?)
                """, (nombre_equipo, hora_formateada, fecha_formateada))
conn.commit()

# Envio de notificación por Pushbullet
Titulo = "Inicio del dispositivo"
Descripcion = f"El equipo 💻 {nombre_equipo} se ha iniciado a las ⏲️ {hora_formateada}."

pb.push_note(Titulo, Descripcion)

# Cerrar conexión a la base de datos
cursor.close()
conn.close()