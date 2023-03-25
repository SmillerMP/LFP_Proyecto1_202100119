import math


listaArbol = []
listaConfiguracionDot = []
listaErrores = [] 

def get_listaArbol():
    return listaArbol

def get_listaErrores():
    return listaErrores

def get_listaConfiguracionDot():
    return listaConfiguracionDot


class Analizador:
    def __init__(self, entrada):
        self.texto = entrada 
        self.index = 0 
        self.fila = 1 
        self.columna = 1 
        self.contadorHijo = 0
        self.contadorGeneral = 0


    def _compilador(self):
        estado_actual = 'S0'
        while self.texto[self.index] != "":
            self.columna += 1
            #print(f'CARACTER11 - {self.texto[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')
            
            # Indentifica los saltos de linea
            if self.texto[self.index] == '\n':
                self.fila += 1
                self.columna =0

            # ************************
            #         ESTADOS
            # ************************

            
            # S0 -> { S1
            elif estado_actual == 'S0':
                estado_actual = self._token('{', 'S0', 'S1')

            # S1 -> "Operacion" S2
            elif estado_actual == 'S1':
                if self.texto[self.index] != " ":
                    a = self._operaciones('S14')
                    estado_actual = a[0]
                    self.contadorGeneral += 1
                    self.contadorHijo = 0
                    # print("\t*****RESULTADO*****")
                    # print('\t',a[1])
                    # print('\t*******************************\n')

            # S14 -> } S15
            elif estado_actual == 'S14':
                #print("ESTO DE ULTIMO")
                estado_actual = self._token('}', 'S14', 'S15')

            # S15 -> , S0
            #       | Lineas finales
            elif estado_actual == 'S15':
                if self.texto[self.index] != ' ':
                    estado_actual = self._token(',', 'S15', 'S0')
                    # If si error en estado actual, pasa a compile
                    if estado_actual == "ERROR":
                        estado_actual = self._lineasFinales('S18')

                    
            elif estado_actual == 'S25':  
                break
            

            if estado_actual == 'ERROR':
                #print('\t AQUI OCURRIO UN ERROR')
                estado_actual = 'S0'
            
            if self.index < len(self.texto) - 1:
                self.index +=1
            else:
                break


        
    def _digito(self, estado_siguiente):
        estado_actual = 'D0'
        numero = ""
        while self.texto[self.index] != "":
            #print(f'CARACTER - {self.texto[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')

            # IDENTIFICAR SALTO DE LINEA
            if self.texto[self.index] == '\n':
                self.fila += 1
                self.columna =0

            
            # PARA SALIRSE
            elif str(self.texto[self.index])== '"':
                self.index -= 1
                return [estado_siguiente, numero]
            elif str(self.texto[self.index])== ']':
                self.index -= 1
                return [estado_siguiente, numero]
            elif str(self.texto[self.index])== '}':
                self.index -= 1
                return [estado_siguiente, numero]

            # VERIFICAR SI ES DECIMAL
            elif self.texto[self.index] == '.':
                token = "."
                if estado_actual == 'D2' or estado_actual == 'D0':
                    estado_actual = 'ERROR'
                elif self.texto[self.index] != ' ':
                    text = self._juntar(self.index, len(token))
                    if self._analizar(token, text):
                        numero += text
                        estado_actual = 'D2'
                        self.index += len(token) - 1
                        self.columna += len(token) - 1
                    else:
                        estado_actual = 'ERROR'


            # ************************
            #         ESTADOS
            # ************************

            # D0 -> [0-9] D0 
            elif estado_actual == 'D0' or estado_actual == 'D1':
                if self.texto[self.index] != ' ':
                    estado_actual = 'ERROR'
                    for i in ['0','1','2','3','4','5','6','7','8','9']:
                        token = i
                        text = self._juntar(self.index, len(token))
                        if self._analizar(token, text):
                            numero += text
                            estado_actual = 'D1'
                            break

            # D2 -> [0-9] D2
            elif estado_actual == 'D2':
                if self.texto[self.index] != ' ':
                    estado_actual = 'ERROR'
                    for i in ['0','1','2','3','4','5','6','7','8','9']:
                        text = self._juntar(self.index, len(i))
                        if self._analizar(i, text):
                            numero += text
                            estado_actual = 'D2'
                            break

            # ERRORES 
            if estado_actual == 'ERROR':
                return ['ERROR', -1]
            
            #INCREMENTAR POSICION
            if self.index < len(self.texto) - 1:
                self.index +=1
            else:
                break
    

    def _lineasFinales(self, estado_siguiente):
        estado_actual = 'S16'
        color = ''
        valorIzquierdo = ''
        while self.texto[self.index] != "":
            #print(f'CARACTER OP - {self.texto[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')
            
            if self.texto[self.index] == '\n':
                self.fila += 1
                self.columna = 0

            # ************************
            #     ESTADOS FINALES
            # ************************

            
            # S -> "Operacion" S2
            elif estado_actual == 'S16':
                estado_actual = self._token('"Color-Fondo-Nodo"', 'S16', 'S17')
                valorIzquierdo = 'Color-Fondo-Nodo'
            
            # S2 -> : S3
            elif estado_actual == 'S17':
                estado_actual = self._token(':', 'S17', 'S18')

            elif estado_actual == 'S18':
                colores = ['"Rojo"','"Amarillo"', '"Azul"', '"Negro"', '"Verde"', '"Blanco"']
                for i in colores:
                    estado_actual = self._token(i, 'S18', 'S19')
                    if estado_actual == 'S19':
                        listaTemp = [valorIzquierdo ,i]
                        listaConfiguracionDot.append(listaTemp)
                        break
                    if estado_actual != 'ERROR':
                        color = i
                        break
            
            elif estado_actual == 'S19':
                estado_actual = self._token('"Color-Fuente-Nodo"', 'S19', 'S20')
                valorIzquierdo = 'Color-Fuente-Nodo'

            elif estado_actual == 'S20':
                estado_actual = self._token(':', 'S20', 'S21')

            elif estado_actual == 'S21':
                colores = ['"Rojo"','"Amarillo"', '"Azul"', '"Negro"', '"Verde"', '"Blanco"']
                for i in colores:
                    estado_actual = self._token(i, 'S21', 'S22')
                    if estado_actual == 'S22':
                        listaTemp = [valorIzquierdo ,i]
                        listaConfiguracionDot.append(listaTemp)
                        break

                    if estado_actual != 'ERROR':
                        color = i
                        break

            elif estado_actual == 'S22':
                estado_actual = self._token('"Forma-Nodo"', 'S22', 'S23')
                valorIzquierdo = 'Forma-Nodo'
            
            # S2 -> : S3
            elif estado_actual == 'S23':
                estado_actual = self._token(':', 'S23', 'S24')

            elif estado_actual == 'S24':
                colores = ['"Circulo"','"Cuadrado"', '"Triangulo"']
                for i in colores:
                    estado_actual = self._token(i, 'S24', 'S25')
                    if estado_actual == 'S25':
                        listaTemp = [valorIzquierdo ,i]
                        listaConfiguracionDot.append(listaTemp)
                        break

                    if estado_actual != 'ERROR':
                        color = i
                        break
            
            
            # Incrementar posicion
            if self.index < len(self.texto) - 1:
                self.index +=1
            else:
                break

    def _operaciones(self, estado_siguiente):
        estado_actual = 'S1'
        hijo_derecho = ""
        hijo_izquierdo = ""
        operador = ""
        while self.texto[self.index] != "":
            #print(f'CARACTER OP - {self.texto[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')
            
            # IDENTIFICAR SALTO DE LINEA
            if self.texto[self.index] == '\n':
                self.fila += 1
                self.columna = 0

            # ************************
            #         ESTADOS
            # ************************

            
            # S1 -> "Operacion" S2
            elif estado_actual == 'S1':
                estado_actual = self._token('"Operacion"', 'S1', 'S2')
            
            # S2 -> : S3
            elif estado_actual == 'S2':
                estado_actual = self._token(':', 'S2', 'S3')

            # S3 -> OPERADOR S4
            elif estado_actual == 'S3':
                operadores = ['"Suma"','"Resta"', '"Division"', '"Multiplicacion"', '"Potencia"', 
                            '"Raiz"', '"Mod"', '"Inverso"', '"Seno"', '"Coseno"', '"Tangente"']
                for i in operadores:
                    estado_actual = self._token(i, 'S3', 'S4')
                    if estado_actual != 'ERROR':
                        operador = i
                        break

            # S4 -> "Valor1" S5
            elif estado_actual == 'S4':
                estado_actual = self._token('"Valor1"', 'S4', 'S5')

            # S5 -> : S6
            elif estado_actual == 'S5':
                estado_actual = self._token(':', 'S5', 'S6')

            # S6 -> DIGITO S9 
            #    | [ S7
            elif estado_actual == 'S6':
                estado_actual = self._token('[','S6','S7')
                if estado_actual == 'ERROR':
                    estado_actual = 'S9'
                    a = self._digito('S9')
                    if "ERROR" == a[0]:
                        estado_actual = 'ERROR'
                    elif a[0] == 'S9':
                        hijo_izquierdo = a[1]

            # S7 -> S1 S8
            elif estado_actual == 'S7':
                a = self._operaciones('S8')
                estado_actual = a[0]
                hijo_izquierdo = a[1]

            # S8 -> ] S9
            elif estado_actual == 'S8':
                estado_actual = self._token(']','S8','S9')
                

            # S9 -> "Valor2" S10
            elif estado_actual == 'S9':
                if operador == '"Inverso"' or operador == '"Seno"'  or operador == '"Coseno"'  or operador == '"Tangente"':
                    self.index -= 1
                    # REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                    # print("\t*****OPERACION ARITMETICA*****")
                    # print('\t',operador ,'(',hijo_izquierdo ,')' )
                    # print('\t*******************************\n')

                    self.contadorHijo += 1
                    resultadoMatematico = self._operecacionesSimples(hijo_izquierdo, operador)
                    listaTemp = [self.contadorGeneral, self.contadorHijo ,operador, resultadoMatematico, hijo_izquierdo]
                    listaArbol.append(listaTemp)
                    
                    return ['S14', resultadoMatematico]  
                else:
                    estado_actual = self._token('"Valor2"', 'S9', 'S10')

            # S10 -> : S11
            elif estado_actual == 'S10':
                estado_actual = self._token(':', 'S10', 'S11')

            # S11 -> DIGITO S14 
            #    | ] S12
            elif estado_actual == 'S11':
                estado_actual = self._token('[','S11','S12')
                if estado_actual == 'ERROR':
                    estado_actual = 'S14'
                    a = self._digito('S14')
                    if "ERROR" == a[0]:
                        estado_actual = 'ERROR'
                    elif 'S14' == a[0]:
                        hijo_derecho = a[1]
                        # Realiza las operacion con un solo valor
                        # print("\t*****OPERACION ARITMETICA*****")
                        # print('\t',hijo_izquierdo , operador, hijo_derecho)
                        # print('\t*******************************\n')

                        resultadoMatematico = self._operecacionesDobles(hijo_izquierdo, hijo_derecho, operador)

                        self.contadorHijo += 1
                        

                        listaTemp = [self.contadorGeneral, self.contadorHijo ,operador, resultadoMatematico, hijo_izquierdo, hijo_derecho]
                        listaArbol.append(listaTemp)
                        
                        return [estado_siguiente, resultadoMatematico]
                    
        
                        
                    

            # S12 -> S1 S13
            elif estado_actual == 'S12':
                estado_actual = 'S13'
                a = self._operaciones('S13')
                hijo_derecho = a[1]
                if "ERROR" == a[1]:
                    estado_actual = 'ERROR'

            # S13 -> } S14
            elif estado_actual == 'S13':
                estado_actual = self._token(']','S13','S14')

                # Realiza la operacion con 2 valores
                # print("\t*****OPERACION ARITMETICA*****")
                # print('\t',hijo_izquierdo , operador, hijo_derecho)
                # print('\t*******************************\n')

                resultadoMatematico = self._operecacionesDobles(hijo_izquierdo, hijo_derecho, operador)
                self.contadorHijo += 1

                listaTemp = [self.contadorGeneral, self.contadorHijo ,operador, resultadoMatematico, hijo_izquierdo, hijo_derecho]
                listaArbol.append(listaTemp)

                return [estado_siguiente, resultadoMatematico]  



            
            # ERRORES 
            if estado_actual == 'ERROR':
                # print("********************************")
                # print("\tERROR")
                # print("********************************")
                
                # Guarda los errores
                self._errores(self.texto[self.index], self.fila, self.columna)
                return ['ERROR', -1]
            
            # Incrementar posicion
            if self.index < len(self.texto) - 1:
                self.index +=1
            else:
                break

    

    def _token(self, token, estado_actual, estado_siguiente):
        if self.texto[self.index] != " ":
            text = self._juntar(self.index, len(token))
            if self._analizar(token, text):
                self.index += len(token) - 1
                self.columna += len(token) - 1
                return estado_siguiente
            else:
                return 'ERROR'
        else:
            return estado_actual
        

    def _juntar(self,indice, contador):
        try:
            tmp = ''
            for i in range(indice, indice + contador):
                tmp += self.texto[i]
            return tmp
        except:
            return None
        
    def _analizar(self, token, texto):
        try:
            count = 0
            tokem_tmp = ""
            for i in texto:
                #print('COMBINACION -> ',i , '==', token[count])
                if str(i) == str(token[count]):
                    tokem_tmp += i  
                    count += 1 
                else:
                    #print('ERROR1')
                    return False
                
            #print(f'********** ENCONTRE - {tokem_tmp} ***************')
            return True
        except:
            #print('ERROR2')
            return False

    def _errores(self, token, fila, columna):
        listaErrores.append({"token":token, "fila": fila, "columna":columna})


    # Operaciones Matematicas con dos valores a utilizar
    def _operecacionesDobles(self, izquierda, derecha, operacion):
        izquierda = float(izquierda)
        derecha = float(derecha)

        if operacion == '"Suma"':
            resultado = izquierda + derecha
        
        # Operacion Resta
        elif operacion == '"Resta"':
            resultado = izquierda - derecha
            
        elif operacion == '"Multiplicacion"':
            resultado = izquierda * derecha

        elif operacion == '"Division"':
            resultado = izquierda / derecha
        
        elif operacion == '"Potencia"':
            resultado = izquierda ** derecha
        
        elif operacion == '"Raiz"':
            resultado = izquierda ** (1/derecha )

        elif operacion == '"Mod"':
            resultado = izquierda % derecha

        

        resultado = round(resultado, 3)
        return resultado
    
    # Operaciones Simples con un solo valor, como Coseno, Seno, Tangente
    def _operecacionesSimples(self, izquierda, operador):
        izquierda = float(izquierda)

        if operador == '"Inverso"':
            resultado = izquierda ** (-1)
        
        elif operador == '"Seno"':
            izquierda = izquierda*(math.pi/180)
            resultado = math.sin(izquierda)
        
        elif operador == '"Coseno"':
            izquierda = izquierda*(math.pi/180)
            resultado = math.cos(izquierda)
        
        elif operador == '"Tangente"':
            izquierda = izquierda*(math.pi/180)
            resultado = math.tan(izquierda)

        resultado = round(resultado, 3)
        return resultado


 

