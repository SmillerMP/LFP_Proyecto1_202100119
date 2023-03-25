import json


def generadorJson(lista):
    listaNueva = []
    contador = 0

    if len(lista) != 0:
        for x in lista:
            contador += 1

            datos = {
                "No.":contador,
                "Descripcion-Token": {
                    "Lexema":x["token"],
                    "Tipo":"Error",
                    "Columna":x["columna"],
                    "Fila":x["fila"]
                }
            }
            listaNueva.append(datos)
        

        # Escribir la lista de diccionarios en un archivo JSON
        with open('Resultados\ERRORES_202100119.json', 'w') as lineas:
            json.dump(listaNueva, lineas, indent=4)

    else:
        with open('Resultados\ERRORES_202100119.json', 'w') as lineas:
            lineas.write("[\n]")

            