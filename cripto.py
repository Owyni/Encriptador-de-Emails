import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
import tkinter as tk
import time
import threading
import cifrado
from PIL import Image, ImageTk
from email.message import EmailMessage
import smtplib

class VentanaCarga(ttk.Toplevel):
    def __init__(self, master, imagen_path="logo.png"):
        super().__init__(master)
        self.title("Cifrando email...")
        self.geometry("400x300")
        self.resizable(False, False)
        self.center_window()
        self.configure(bg="#1a1a1a")
        self.wm_iconbitmap('icono.ico')

        contenedor = ttk.Frame(self, bootstyle="dark")
        contenedor.pack(expand=True, fill="both", pady=10)

        try:
            imagen = Image.open(imagen_path)
            imagen = imagen.convert("RGBA")
            imagen = imagen.resize((180, 180), Image.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(imagen)

            self.imagen_label = tk.Label(
                contenedor, image=imagen_tk, bg="#1a1a1a", border=0
            )
            self.imagen_label.image = imagen_tk
            self.imagen_label.pack(pady=10)
        except Exception:
            ttk.Label(contenedor, text="(Imagen no encontrada)", bootstyle="danger").pack(pady=20)

        self.progress = ttk.Progressbar(
            contenedor, bootstyle="success-striped", mode="determinate", length=280
        )
        self.progress.pack(pady=20)
        self.progress["value"] = 0

        self.label_text = ttk.Label(contenedor, text="Cifrando...", bootstyle="light")
        self.label_text.pack()

        threading.Thread(target=self.animar_progreso, daemon=True).start()

    def center_window(self):
        self.update_idletasks()
        width = 400
        height = 300
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def animar_progreso(self):
        for i in range(101):
            time.sleep(0.03)
            self.progress["value"] = i
            self.update_idletasks()
        time.sleep(0.5)
        self.destroy()


class VentanaDestinatario(ttk.Toplevel):

    def __init__(self, master, email_cifrado):
        super().__init__(master)
        self.title("Agregar destinatario")
        self.geometry("350x200")
        self.resizable(False, False)
        self.center_window()
        self.configure(bg="#1a1a1a")
        self.email_cifrado = email_cifrado
        self.wm_iconbitmap('icono.ico')

        ttk.Label(
            self,
            text="Ingrese el correo del destinatario:",
            bootstyle="light",
            font=("Helvetica", 12)
        ).pack(pady=15)

        self.entry_destinatario = ttk.Entry(self, width=40, bootstyle="info")
        self.entry_destinatario.pack(pady=10)

        ttk.Button(
            self,
            text="Guardar y enviar",
            bootstyle="success",
            command=self.guardar_destinatario
        ).pack(pady=15)

    def center_window(self):
        self.update_idletasks()
        width = 350
        height = 200
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def guardar_destinatario(self):
        destinatario = self.entry_destinatario.get().strip()
        remitente = "agonzalez901@uvaq.edu.mx"
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = "TOP SECRET"
        email.set_content(self.email_cifrado)

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(remitente, 'kfsp qgsu ucqp ohqh')
        smtp.send_message(email)

        if not destinatario:
            ToastNotification(
                title="Error",
                message="Debe ingresar un destinatario.",
                alert=True
            ).show_toast()
            return

class VentanaCarga(ttk.Toplevel):
    def __init__(self, master, imagen_path="logo.png"):
        super().__init__(master)
        self.title("Cifrando email...")
        self.geometry("400x300")
        self.resizable(False, False)
        self.center_window()
        self.configure(bg="#1a1a1a")
        self.wm_iconbitmap('icono.ico')

        contenedor = ttk.Frame(self, bootstyle="dark")
        contenedor.pack(expand=True, fill="both", pady=10)

        try:
            imagen = Image.open(imagen_path)
            imagen = imagen.convert("RGBA")
            imagen = imagen.resize((180, 180), Image.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(imagen)

            self.imagen_label = tk.Label(
                contenedor, image=imagen_tk, bg="#1a1a1a", border=0
            )
            self.imagen_label.image = imagen_tk
            self.imagen_label.pack(pady=10)
        except Exception:
            ttk.Label(contenedor, text="(Imagen no encontrada)", bootstyle="danger").pack(pady=20)

        self.progress = ttk.Progressbar(
            contenedor, bootstyle="success-striped", mode="determinate", length=280
        )
        self.progress.pack(pady=20)
        self.progress["value"] = 0

        self.label_text = ttk.Label(contenedor, text="Cifrando...", bootstyle="light")
        self.label_text.pack()

        threading.Thread(target=self.animar_progreso, daemon=True).start()

    def center_window(self):
        self.update_idletasks()
        width = 400
        height = 300
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def animar_progreso(self):
        for i in range(101):
            time.sleep(0.03)
            self.progress["value"] = i
            self.update_idletasks()
        time.sleep(0.5)
        self.destroy()


class VentanaDestinatario(ttk.Toplevel):

    def __init__(self, master, email_cifrado):
        super().__init__(master)
        self.title("Agregar destinatario")
        self.geometry("350x200")
        self.resizable(False, False)
        self.center_window()
        self.configure(bg="#1a1a1a")
        self.email_cifrado = email_cifrado
        self.wm_iconbitmap('icono.ico')

        ttk.Label(
            self,
            text="Ingrese el correo del destinatario:",
            bootstyle="light",
            font=("Helvetica", 12)
        ).pack(pady=15)

        self.entry_destinatario = ttk.Entry(self, width=40, bootstyle="info")
        self.entry_destinatario.pack(pady=10)

        ttk.Button(
            self,
            text="Guardar y enviar",
            bootstyle="success",
            command=self.guardar_destinatario
        ).pack(pady=15)

    def center_window(self):
        self.update_idletasks()
        width = 350
        height = 200
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def guardar_destinatario(self):
        destinatario = self.entry_destinatario.get().strip()
        remitente = "agonzalez901@uvaq.edu.mx"
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = "TOP SECRET"
        email.set_content(self.email_cifrado)

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(remitente, 'kfsp qgsu ucqp ohqh')
        smtp.send_message(email)

        if not destinatario:
            ToastNotification(
                title="Error",
                message="Debe ingresar un destinatario.",
                alert=True
            ).show_toast()
            return

        # Guardar destinatario y texto cifrado
        with open("email_encriptado.txt", "w", encoding="utf-8") as f:
            f.write(f"Destinatario: {destinatario}\n\n")
            f.write("Mensaje cifrado:\n")
            f.write(self.email_cifrado)

        ToastNotification(
            title="Éxito",
            message="Correo enviado, texto y destinatario guardados en 'email_encriptado.txt'.",
            duration=4000
        ).show_toast()
        self.destroy()

class VentanaDesencriptacion(ttk.Toplevel):

    def desencriptar(self):
        try:
            texto_cifrado = self.entry_cifrado.get("1.0", "end-1c").strip()
            texto_limpio = cifrado.descifrar_texto(texto_cifrado)
            self.mostrar_texto_limpio(texto_limpio)
        except Exception as e:
            ToastNotification(
                title="Error de desencriptación",
                message=f"No se pudo desencriptar el texto. {e}",
                alert=True
            ).show_toast()

    def mostrar_texto_limpio(self, texto_limpio):
        ventana_texto_limpio = ttk.Toplevel(self)
        ventana_texto_limpio.title("Texto Desencriptado")
        ventana_texto_limpio.geometry("600x400")
        ventana_texto_limpio.resizable(False, False)
        ventana_texto_limpio.configure(bg="#1a1a1a")
        ventana_texto_limpio.wm_iconbitmap('icono.ico')
        
        ventana_texto_limpio.update_idletasks()
        width = 600
        height = 400
        x = (ventana_texto_limpio.winfo_screenwidth() // 2) - (width // 2)
        y = (ventana_texto_limpio.winfo_screenheight() // 2) - (height // 2)
        ventana_texto_limpio.geometry(f"{width}x{height}+{x}+{y}")

        ttk.Label(
            ventana_texto_limpio,
            text="El texto desencriptado es:",
            bootstyle="light",
            font=("Helvetica", 14)
        ).pack(pady=15)

        texto_widget = tk.Text(ventana_texto_limpio, wrap="word", width=70, height=15, state="normal")
        texto_widget.insert(tk.END, texto_limpio)
        texto_widget.config(state="disabled")
        texto_widget.pack(pady=10)

        ttk.Button(
            ventana_texto_limpio,
            text="Cerrar",
            bootstyle="secondary",
            command=ventana_texto_limpio.destroy
        ).pack(pady=10)


    def __init__(self, master):
        super().__init__(master)
        self.title("Ingrese mensaje a desencriptar")
        self.geometry("800x600")
        self.resizable(False, False)
        self.center_window()
        self.configure(bg="#1a1a1a")
        self.wm_iconbitmap('icono.ico')

        ttk.Label(
            self,
            text="Ingrese el texto cifrado:",
            bootstyle="light",
            font=("Helvetica", 14)
        ).pack(pady=15)

        self.entry_cifrado = ttk.Text(self, width=80, height=15)
        self.entry_cifrado.pack(pady=10)

        ttk.Button(
            self,
            text="Desencriptar",
            bootstyle="success",
            command=self.desencriptar
        ).pack(pady=20)

        ttk.Button(
            self,
            text="Menú Principal",
            bootstyle="secondary",
            command=self.destroy
        ).pack(pady=20)

    def center_window(self):
        self.update_idletasks()
        width = 800
        height = 600
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")


# ========================= INTERFAZ PRINCIPAL =========================
root = ttk.Window(themename="vapor")
root.title("Encriptador de Mails: Created by Owynn")
root.geometry("800x600")
x = (root.winfo_screenwidth() // 2) - (800 // 2)
y = (root.winfo_screenheight() // 2) - (600 // 2)
root.geometry(f"+{x}+{y}")

root.wm_iconbitmap('icono.ico')

label = ttk.Label(root, text="Bienvenido al encriptador de EMAILS!",
                  bootstyle="default", font=("Helvetica", 20))
label.pack(pady=20)

label2 = ttk.Label(root, text="Redacte el email a encriptar:",
                   bootstyle="light", font=("Helvetica", 14))
label2.pack(pady=10)

entry = ttk.Text(root, width=80, height=15)
entry.pack(pady=10)

toast = ToastNotification(
    title='Error',
    message="Por favor, ingrese un email para encriptar.",
    alert=True,
    duration=5000
)


def go():
    email_text = entry.get("1.0", tk.END).strip()

    if not email_text:
        toast.show_toast()
        return

    try:
        root.withdraw()

        ventana_carga = VentanaCarga(root, imagen_path="logo.png")
        ventana_carga.wait_window()  # Espera a que termine la carga

        email_cifrado = cifrado.cifrar_texto(email_text)

        # Mostrar ventana para agregar destinatario
        ventana_dest = VentanaDestinatario(root, email_cifrado)
        ventana_dest.wait_window()

    except Exception as e:
        ToastNotification(title="Error", message=str(e), alert=True).show_toast()

    finally:
        root.deiconify()

def decripter():
    try:
        root.withdraw()
        ventana_des = VentanaDesencriptacion(root)
        ventana_des.wait_window()

    except Exception as e:
        ToastNotification(title="Error", message=str(e), alert=True).show_toast()
    
    finally:
        root.deiconify()


button = ttk.Button(root, text="Encriptar Email", bootstyle="success", command=go)
button.pack(pady=20)

button = ttk.Button(root, text="Modo Desencriptador", bootstyle="success", command=decripter)
button.pack(pady=10)

root.mainloop()