import os
from pathlib import *
from tkinter import filedialog
import tkinter as tk


def abrir_Archivo(cajaTexto):
    nombreArchivo = filedialog.askopenfilename(
        filetypes={
            ("Archivos de texto", "*.txt"),
            ("Archivos de Python", ("*.py", "*.pyx")),
            ("Todos los archivos", "*.*")
        }
    )

    if nombreArchivo:

        with open(nombreArchivo, 'r') as f:
            content = f.read()
            cajaTexto.delete('1.0', tk.END)
            cajaTexto.insert(tk.END, content)
    else:
        print("No se ha seleccionado ningún archivo.")

