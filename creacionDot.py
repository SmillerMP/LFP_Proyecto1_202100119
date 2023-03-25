
import os

def creacionArbol(lista, listaConfiguracion):

    def color(color):
        limpio = color.replace('"', '')
        if limpio == 'Rojo':
            return 'red'
        
        elif limpio == 'Amarillo':
            return 'yellow'

        elif limpio == 'Azul':
            return 'blue'
        
        elif limpio == "Negro":
            return 'black'
        
        elif limpio == 'Verde':
            return 'green'
        
        elif limpio == 'Blanco':
            return 'white'
        
    colorNodo = color(listaConfiguracion[0][1])
    colorFuente = color(listaConfiguracion[1][1])
    formaNodo = color(listaConfiguracion[2][1])

    

    grafo_dot = open("Resultados\RESULTADOS_202100119.dot", "w")
    grafo_dot.write('digraph { \n')
    grafo_dot.write('rankdir = TB \n' )
    grafo_dot.write(f'node[shape=circle, style="filled" fontname="Arial", fontsize=12, fontcolor="{colorFuente}", fillcolor="{colorNodo}"] \n\n')


    contador = 1
    valorDerecho = False
    valorIzquierdo = False
    contador2 = 1
    primero = 0
    
    maximiliano = len(lista)
    for x in lista:
        maximo = lista[primero][1]
        general = lista[primero][0]

        #print(contador)
        textoLimpio = x[2].replace('"', '')
        
        # Para Datos con Operaciones con 2 Valores
        if len(x) == 6:
            for i in range(contador2,  maximiliano):

                #print(i)
                # Hijo Izquierdo
                if x[4] == lista[i][3] and x[0] == general:
                    if valorIzquierdo == False:
                        grafo_dot.write(f"N{x[0]}{x[1]} -> N{lista[i][0]}{lista[i][1]} \n")
                        valorIzquierdo = True
                        break
                        

            for j in range(contador2, maximiliano):
                # Hijo Derecha
                if x[5] == lista[j][3] and x[0] == general:
                    if valorDerecho == False:
                        grafo_dot.write(f"N{x[0]}{x[1]} -> N{lista[j][0]}{lista[j][1]} \n")
                        valorDerecho = True
                        break

            # Cambia el Label para el nodo en caso de que sea un resultado
            grafo_dot.write(f'N{x[0]}{x[1]}[label="{textoLimpio}:\n{x[3]}"]\n')


            # Agrega las hojas der arbol, o los ultimos datos de las ramas
            # Hijo Izquierdo
            if  valorIzquierdo == False:
                grafo_dot.write(f"N{x[0]}{x[1]} -> V{x[0]}{x[1]}1 \n")
                grafo_dot.write(f'V{x[0]}{x[1]}1[label="{x[4]}"]\n')
            else:
                valorIzquierdo = False
        
            # Hijo Derecho
            if valorDerecho == False:
                grafo_dot.write(f"N{x[0]}{x[1]} -> V{x[0]}{x[1]}2 \n")
                grafo_dot.write(f'V{x[0]}{x[1]}2[label="{x[5]}"]\n')
            else:
                valorDerecho = False

            contador += 1
            contador2 += 1

            #print(contador)
            
            if contador > maximo:
                primero = contador2-1
                contador = 1
                grafo_dot.write('\n\n//!---------------NUEVO ARBOL ----------------!\n\n')

        # Operaciones con solo un digito
        if len(x) == 5:
            for i in range(contador2,  maximiliano):

                #print(i)
                # Hijo Izquierdo
                if x[4] == lista[i][3] and x[0] == general:
                    if valorIzquierdo == False:
                        grafo_dot.write(f"N{x[0]}{x[1]} -> N{lista[i][0]}{lista[i][1]} \n")
                        valorIzquierdo = True
                        break
                        

            # Cambia el Label para el nodo en caso de que sea un resultado
            grafo_dot.write(f'N{x[0]}{x[1]}[label="{textoLimpio}:\n{x[3]}"]\n')


            # Agrega las hojas der arbol, o los ultimos datos de las ramas
            # Hijo Izquierdo
            if  valorIzquierdo == False:
                grafo_dot.write(f"N{x[0]}{x[1]} -> V{x[0]}{x[1]}1 \n")
                grafo_dot.write(f'V{x[0]}{x[1]}1[label="{x[4]}"]\n')
            else:
                valorIzquierdo = False
        

            contador += 1
            contador2 += 1

            #print(contador)
            
            if contador > maximo:
                primero = contador2-1
                contador = 1
                grafo_dot.write('\n\n//!---------------NUEVO ARBOL ----------------!\n\n')


    

    grafo_dot.write('\n\n}')
        
    os.system("dot.exe -Tpdf Resultados/RESULTADOS_202100119.dot -o  Resultados/RESULTADOS_202100119.pdf")

        
            