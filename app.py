import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# Importamos Messagebox para poder mostrar la ventana emergente
from ttkbootstrap.dialogs import Messagebox

def mostrar_datos():
    # Extraemos el texto de los campos de entrada
    usuario = entrada_usuario.get()
    password = entrada_password.get()
    
    # Creamos el texto del mensaje
    mensaje = f"Usuario ingresado: {usuario}\nContraseña ingresada: {password}"
    
    # Mostramos la alerta en pantalla
    Messagebox.show_info(title="Datos Recibidos", message=mensaje)

# Configuración de la ventana principal
root = ttk.Window(themename="darkly")
root.title("Mi App")
root.geometry("500x300")

# Campo de Usuario
ttk.Label(root, text="Usuario:").pack(pady=5)
entrada_usuario = ttk.Entry(root)
entrada_usuario.pack(pady=5)

# Aplicamos el autofocus
entrada_usuario.focus_set()

# Campo de Contraseña
ttk.Label(root, text="Contraseña:").pack(pady=5)
entrada_password = ttk.Entry(root, show="*")
entrada_password.pack(pady=5)

# Botón de Iniciar Sesión (Conectado a la función mediante 'command')
ttk.Button(
    root, 
    text="Iniciar Sesión", 
    bootstyle="success", 
    command=mostrar_datos
).pack(pady=15)

root.mainloop()