import os
from pathlib import *
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox as MessageBox

nombreArchivo = None

def abrir_Archivo(cajaTexto):
    global nombreArchivo
    nombreArchivo = filedialog.askopenfilename(
        # Archivos compatibles
        filetypes={
            ("Archivos de texto", "*.txt"),
            ("Archivos de Python", ("*.py", "*.pyx")),
            ("Todos los archivos", "*.*")
        }
    )


    if nombreArchivo:
        try:
            # Lectura del archivo y escritura en la caja de texto
            with open(nombreArchivo, 'r') as lineas:
                content = lineas.read()

                #cajaTexto.delete('1.0', tk.END)
                cajaTexto.insert(tk.END, content + "\n")
        except:
            # Mensaje de error en caso que el archivo no se pueda leer
            MessageBox.showerror("Error", "Asegurese de abrir un archivo de tipo texto")

    else:
        MessageBox.showwarning("Alerta", "No se a seleccionado ningun archivo.")


def limpiar(cajaTexto):
    
    # Confirmacion en caso que se desee limpiar
    confirmacion = MessageBox.askyesno("Confirmar", "¿Desea Limpiar la Caja de Texto?")

    if confirmacion:
        cajaTexto.delete('1.0', tk.END)
        MessageBox.showinfo("Mensaje", "Limpieza realizada con Exito!")


# Guardar el texto en la ruta especificada anteriormente
def guardar(cajaTexto):

    # Verifica que exista una ruta para guardar el archivo
    if nombreArchivo == None:
        MessageBox.showerror("Error", "No se ha encontrado una ruta para guardar el archivo!")

    else:
        # Abre el archivo y escribe todos los datos existentes en la caja de texto
        with open(nombreArchivo, 'w') as lineas:
            contenido = cajaTexto.get("1.0", tk.END)
            lineas.write(contenido)
            MessageBox.showinfo("Mensaje", "Se guardo correctamente los datos en la ruta: " + str(nombreArchivo))
