**Bienvenido a mi aplicación de escritorio para enviar emails encriptados usando un sistema de cifrado propio basado en un diccionario de sustitución.
El proyecto está desarrollado en python, la interfáz gráfica utiliza ttkbootstrap con el tema Vaporwave.**

# La aplicación permite:

- ✍️ Redactar un correo dentro de la app

- 🔐 Encriptarlo usando un diccionario personalizado

- 📤 Enviarlo directamente por email (via SMTP)

- 📥 Guardar destinatario y mensaje cifrado

- 🔓 Desencriptar mensajes previamente cifrados

# 🔧 Tecnologías y librerías utilizadas:

## 🪄 ttkbootstrap (UI principal)
Framework basado en Tkinter con estilos modernos, temas, botones animados y componentes avanzados.
🔗 Wiki: https://github.com/israel-dryer/ttkbootstrap/wiki

## 📨 smtplib (envío de correos)
Librería estándar de Python para enviar emails a través de servidores SMTP.
🔗 Documentación: https://docs.python.org/3/library/smtplib.html

## 🖼️ Pillow (gestión de imágenes)
Usado para cargar, convertir y mostrar imágenes (como el logo animado).
🔗 Docs: https://pillow.readthedocs.io/en/stable/

# 🔐 Método de cifrado:
El cifrado está definido en el archivo cifrado.py, donde cada letra del alfabeto se sustituye por otra según un diccionario propio creado desde cero.
La aplicación permite tanto cifrar como descifrar, y funciona con mayúsculas, minúsculas y saltos de línea.

> 🖥️ Características principales
>
> 🧼 Interfaz limpia estilo vaporwave **(ttkbootstrap)**
>
> ⏳ Ventana de carga animada
>
> 📝 Redacción de correos en un editor tipo bloc de notas
>
> 🔐 Cifrado instantáneo
>
> 📬 Ventana dedicada para agregar destinatario
>
> ✔️ Notificaciones tipo Toast
>
> 📁 Guarda automáticamente el mensaje cifrado en un archivo TXT
>
> 🔓 Modo de desencriptación independiente
