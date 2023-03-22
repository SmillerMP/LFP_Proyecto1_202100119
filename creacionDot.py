
from analizador import *

analizar()

listaDatos = get_listaArbol()

listaReverso = list(reversed(listaDatos))

for i in listaReverso:
    print(i)

def creacionDot(lista):

    grafo_dot = open("RESULTADOS_202100119.dot", "w")
    grafo_dot.write('digraph { \n')
    grafo_dot.write('rankdir = TB \n' )
    grafo_dot.write('node[shape=circle, fontname="Arial", fontsize=12] \n\n')


    contador = 1
    valorDerecho = False
    valorIzquierdo = False
    contador2 = 1
    primero = 0
    
    maximiliano = len(lista)
    print(maximiliano)
    for x in lista:
        maximo = listaReverso[primero][1]
        general = listaReverso[primero][0]

        #print(contador)
        textoLimpio = x[2].replace('"', '')

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


        grafo_dot.write(f'N{x[0]}{x[1]}[label="{textoLimpio}:\n{x[3]}"]\n')


        if  valorIzquierdo == False:
            grafo_dot.write(f"N{x[0]}{x[1]} -> V{x[0]}{x[1]}1 \n")
            grafo_dot.write(f'V{x[0]}{x[1]}1[label="{x[4]}"]\n')
        else:
            valorIzquierdo = False
       
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


    # for x in lista:
        
    #     if len(x) == 6:
    #         textoLimpio = x[2].replace('"', '')
     
    #         grafo_dot.write(f"N{x[0]}{x[1]} -> V{x[0]}{x[1]}1 \n")
    #         grafo_dot.write(f"N{x[0]}{x[1]} -> V{x[0]}{x[1]}2 \n")


    #         grafo_dot.write(f'N{x[0]}{x[1]}[label="{textoLimpio}:\n{x[3]}"]\n')
    #         grafo_dot.write(f"V{x[0]}{x[1]}1[label={x[4]}] \n")
    #         grafo_dot.write(f"V{x[0]}{x[1]}2[label={x[5]}] \n")

    

    grafo_dot.write('\n\n}')
        


        
            
creacionDot(listaReverso)