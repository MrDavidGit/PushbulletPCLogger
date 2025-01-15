# PushbulletPCLogger

**PushbulletPCLogger** es un proyecto que consiste en dos scripts simples que permiten recibir notificaciones en tu dispositivo cuando un ordenador se **enciende** o se **apaga**.

## ¿Por qué hice esta idea?
La idea se me ocurrio de repende, porque pense que seria curioso y util en algunos casos, que recibiera una notificación en el movil cuando se encendia o apagara mi ordenador.

Aunque hice este pequeño proyecto mas como practica personal y de aprendizaje porque me gusta probar cosas, creo que tambien puede serle útil a algunas personas para monitorear cuando se enciende un ordenador suyo, sea porque lo comparten con alguien o como herramienta de monitoreo parental.

Este proyecto fue creado con la ayuda de la IA, especificamente de chatgpt 4o, que me ayudo a entender como hacer los scripts usando la api de pushbullet y la conexión a la base de datos entre otras pequeñas cosas.
Tambien me ayudo a escribir este readme dado mi falta de experiencia en ello para estructurarlo.

---

## Tecnologías y librerías usadas

- **Python 3**: Lenguaje usado para los scripts.
- **Pushbullet API**: API de la app Pushbullet usada para enviar las notificaciones al dispositivo móvil.
- **MariaDB**: La base de datos usada para almacenar los datos de encendido y apagado del sistema .
- **Programador de tareas de Windows**: Para ejecutar el script de encendido en Windows.
- **gpedit.msc**: Para ejecutar el script de apagado en Windows.
- **El cron jobs de Linux**: Para ejecutar los scripts de apagado en Linux.

---

## Instalación

### 1. **Clona el repositorio**
Primero, clona el repositorio en tu máquina local:
```bash
git clone https://github.com/tu-usuario/PushbulletPCLogger.git
cd PushbulletPCLogger
```

### 2. **Instala las dependencias**
Asegúrate de tener **pip** instalado en tu sistema y usa el siguiente comando para instalar las librerías necesarias:
```bash
pip install -r requirements.txt
```

### 3. **Configura la base de datos MariaDB**
1. Localiza el archivo **.env.example** y renómbralo a **.env**.
2. Dentro del archivo **.env**, asegúrate de configurar las credenciales necesarias para los scripts:
```plaintext
DB_HOST=localhost
DB_PORT=3306
DB_NAME=tu_base_de_datos
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña

API_KEY=tu_clave_de_pushbullet

```

### 4. **Obten la clave de la API de Pushbullet**
- Inicia sesión en [Pushbullet](https://www.pushbullet.com).
- En la sección de opciones, busca **Create Access Token** para generar tu clave de la API (token). 
- Copia y pega este token en tu archivo `.env` en 'API_KEY='.

---

## Configuración en Windows

### 1. Script de encendido
Para ejecutar el script de encendido en Windows, utiliza el **Programador de Tareas**:

1. Abre el Programador de Tareas (taskschd.msc).
2. Haz clic en **Crear tarea**.
3. En la pestaña **General**, asigna un nombre, por ejemplo: "Notificación de encendido".
4. En la pestaña **Desencadenadores**, haz clic en **Nuevo** y selecciona **Al iniciar el equipo**.
5. En la pestaña **Acciones**, haz clic en **Nueva...** y selecciona el script de Python para el encendido.
6. Haz clic en **Aceptar** y guarda la tarea.

### 2. Script de apagado
Para ejecutar el script de apagado en Windows, debes usar el **Editor de directivas de seguridad local (gpedit.msc)**:

1. Pulsa **Windows + R** y escribe `gpedit.msc`.
2. Ve a **Configuración del equipo → Configuración de Windows → Scripts (Inicio/Apagado)**.
3. Haz doble clic en **Apagado**, luego haz clic en **Agregar** y selecciona el script de apagado.

---

## Configuración en Linux

### 1. Script de encendido en Linux
Para que el script de encendido se ejecute automáticamente al iniciar (o reiniciar) el sistema, puedes usar **Cron Jobs** con la directiva `@reboot`:

1. Abre una terminal.
2. Escribe `crontab -e` para editar las tareas programadas.
3. Añade la siguiente línea al final del archivo (ajustando la ruta a tu script):
   ```bash
   @reboot /ruta/al/script_de_encendido.py
   ```
4. Guarda y cierra el archivo.

### 2. Script de apagado en Linux
Igual que con el script de encendido, añade en el archivo de cronjobs esta linea:
   ```bash
   @shutdown /ruta/al/script_de_apagado.py
   ```
> **Nota**: La directiva `@shutdown` no es estándar en muchos sistemas. Algunas distribuciones necesitan otros enfoques por lo que si tu sistema no soporta esa directiva, considera configurar un servicio **systemd** para que se ejecute en el apagado del dispositivo

---

¡Listo! Con estos pasos, tendrás configurados los scripts de encendido y apagado tanto en Windows o en Linux.


> **Nota**: Reiniciar el equipo cuenta como un nuevo inicio; por lo tanto, el script de encendido se ejecutará siempre que el sistema se encienda o se reinicie.