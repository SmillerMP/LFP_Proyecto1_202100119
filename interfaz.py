import tkinter as tk
from funcionesGraficas import *

# Funciones
def editorTexto():
    abrir_Archivo(editor)

def limpiarTexto():
    limpiar(editor)

def guardarTexto():
    guardar(editor)

def guardarComoTexto():
    guardarComo(editor)



# Creacion de ventana
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Proyecto 1")
ventanaPrincipal.configure(bg="#FC7300")

# Dimensiones de la pantalla
ventanaPrincipal.geometry("1000x600")

# Etiquetas o labels
# Menu principal
tituloPrincipal = tk.Label(ventanaPrincipal, text = "Menu Principal", font = ("Bold", 16), bg = "#00425A", fg="white", pady=4)
tituloPrincipal.pack(fill= tk.X)

titulo_Archivo = tk.Label(ventanaPrincipal, text="Archivo", font = ("Bold", 13), bg = "#1F8A70", padx=50, pady=5)
titulo_Archivo.place(x=600, y=60)

titulo_Ayuda = tk.Label(ventanaPrincipal, text="Ayuda", font = ("Bold", 13), bg = "#1F8A70", padx=55, pady=5)
titulo_Ayuda.place(x=800, y=60)



# Botones
# Abrir
boton_Abrir = tk.Button(ventanaPrincipal, text="Abrir", fon =10, padx=56, bg="#BFDB38", command=editorTexto)
boton_Abrir.place(x=600, y=120)

# Guardar
boton_Guardar = tk.Button(ventanaPrincipal, text="Guardar", font=10, padx=45, bg="#BFDB38", command=guardarTexto)
boton_Guardar.place(x=600, y=170)

# Guardar Como
boton_GuardarComo = tk.Button(ventanaPrincipal, text="Guardar Como", font=10, padx=21, bg="#BFDB38", command=guardarComoTexto)
boton_GuardarComo.place(x=600, y=220)

# Analizar
boton_Analizar = tk.Button(ventanaPrincipal, text="Analizar", font=10, padx=45, bg="#BFDB38")
boton_Analizar.place(x=600, y=270)

# Error
boton_Errores = tk.Button(ventanaPrincipal, text="Errores", font=10, padx=47, bg="#BFDB38")
boton_Errores.place(x=600, y=320)

# Limpiar
boton_Limpiar = tk.Button(ventanaPrincipal, text="Limpiar", font=10, padx=47, bg="#BFDB38", command=limpiarTexto)
boton_Limpiar.place(x=600, y=370)


# Salir
boton_Salir = tk.Button(ventanaPrincipal, text="Salir", command=ventanaPrincipal.destroy, font=10, padx=57, bg="#1F8A70")
boton_Salir.place(x=800, y=370)


# Manual de Usuario
boton_ManualUsuario = tk.Button(ventanaPrincipal, text="Manual de Usuario", font = 10, padx=10, bg="#BFDB38")
boton_ManualUsuario.place(x=800, y=120)

# Manual Tecnico
boton_ManualTec = tk.Button(ventanaPrincipal, text="Manual Tecnico", font=10, padx=20, bg="#BFDB38")
boton_ManualTec.place(x=800, y=170)

# Temas de Ayuda
boton_TemasAyuda = tk.Button(ventanaPrincipal, text="Temas de Ayuda", font=10, padx=16, bg="#BFDB38")
boton_TemasAyuda.place(x=800, y=220)


# Caja de edicion
editor = tk.Text(width=60, height=31)
editor.place(x=50, y=60)

scrollbarEditor = tk.Scrollbar(ventanaPrincipal, command=editor.yview)
scrollbarEditor.place(x=534, y=60, height=500)
# configura el widget Text para que use el scrollbar vertical
editor.config(yscrollcommand=scrollbarEditor.set)


# Bloquer el tama;o de la ventana
ventanaPrincipal.resizable(width=False, height=False)



# Loop ventana
ventanaPrincipal.mainloop()


