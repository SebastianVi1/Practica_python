import tkinter as tk

def mostrar_menu_iniciar_sesion():
    # Limpiar cualquier contenido existente en el frame principal
    for widget in frame_principal.winfo_children():
        widget.destroy()

    # Puedes agregar widgets y funcionalidad específica para el menú de inicio de sesión aquí
    etiqueta_menu = tk.Label(frame_principal, text="Menú de Inicio de Sesión")
    etiqueta_menu.pack(pady=10)

    # Ejemplo: Un botón en el menú de inicio de sesión
    boton_cerrar_sesion = tk.Button(frame_principal, text="Cerrar Sesión", command=cerrar_sesion)
    boton_cerrar_sesion.pack(pady=5)

def cerrar_sesion():
    mensaje.config(text="Sesión cerrada.")

# Funciones para las opciones
def iniciar_sesion():
    mensaje.config(text="Iniciando sesión...")
    mostrar_menu_iniciar_sesion()

def registrarse():
    mensaje.config(text="Registrándose...")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Inicio de Sesión")

# Configurar el tamaño inicial y color de fondo de la ventana
ventana.geometry("400x300")  # Ancho x Altura
ventana.configure(bg="#e6e6e6")  # Color de fondo en formato hexadecimal

# Crear un frame principal para contener el contenido
frame_principal = tk.Frame(ventana, bg="#e6e6e6")
frame_principal.pack(fill=tk.BOTH, expand=True)

# Crear botones para las opciones
boton_iniciar_sesion = tk.Button(frame_principal, text="Iniciar Sesión", command=iniciar_sesion, bg="#4CAF50", fg="white")
boton_iniciar_sesion.pack(pady=5)

boton_registrarse = tk.Button(frame_principal, text="Registrarse", command=registrarse, bg="#008CBA", fg="white")
boton_registrarse.pack(pady=5)

# Widget de etiqueta para mostrar mensajes
mensaje = tk.Label(frame_principal, text="", bg="#e6e6e6")
mensaje.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()