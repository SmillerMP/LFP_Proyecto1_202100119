import tkinter as tk



# Creacion de ventana
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Proyecto 1")
ventanaPrincipal.configure(bg="#fef9e7")

# Dimensiones de la pantalla
ventanaPrincipal.geometry("490x420")

# Etiquetas o labels
# Menu principal
tituloPrincipal = tk.Label(ventanaPrincipal, text = "Menu Principal", font = ("Bold", 16), bg = "#3498db", pady=4)
tituloPrincipal.pack(fill= tk.X)

titulo_Archivo = tk.Label(ventanaPrincipal, text="Archivo", font = ("Bold", 13), bg = "#FFC300", padx=50, pady=5)
titulo_Archivo.place(x=40, y=55)

titulo_Ayuda = tk.Label(ventanaPrincipal, text="Ayuda", font = ("Bold", 13), bg = "#f5b041", padx=55, pady=5)
titulo_Ayuda.place(x=290, y=55)



# Botones
# Abrir
boton_Abrir = tk.Button(ventanaPrincipal, text = "Abrir", font = 10, padx=56, bg="#dc7633")
boton_Abrir.place(x=40, y=120)

boton_Guardar = tk.Button(ventanaPrincipal, text="Guardar", font=10, padx=45, bg="#dc7633")
boton_Guardar.place(x=40, y=170)

boton_GuardarComo = tk.Button(ventanaPrincipal, text="Guardar Como", font=10, padx=21, bg="#dc7633")
boton_GuardarComo.place(x=40, y=220)

boton_Analizar = tk.Button(ventanaPrincipal, text="Analizar", font=10, padx=45, bg="#dc7633")
boton_Analizar.place(x=40, y=270)

boton_Errores = tk.Button(ventanaPrincipal, text="Errores", font=10, padx=47, bg="#dc7633")
boton_Errores.place(x=40, y=320)

boton_Salir = tk.Button(ventanaPrincipal, text="Salir", command=ventanaPrincipal.destroy, font=10, padx=57, bg="#dc7633")
boton_Salir.place(x=40, y=370)



boton_ManualUsuario = tk.Button(ventanaPrincipal, text = "Manual de Usuario", font = 10, padx=10, bg="#FF5733")
boton_ManualUsuario.place(x=290, y=120)

boton_ManualTec = tk.Button(ventanaPrincipal, text="Manual Tecnico", font=10, padx=20, bg="#FF5733")
boton_ManualTec.place(x=290, y=170)

boton_TemasAyuda = tk.Button(ventanaPrincipal, text="Temas de Ayuda", font=10, padx=16, bg="#FF5733")
boton_TemasAyuda.place(x=290, y=220)


# Bloquer el tama;o de la ventana
ventanaPrincipal.resizable(width=False, height=False)

# Loop ventana
ventanaPrincipal.mainloop()