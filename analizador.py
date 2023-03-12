

with open("D:\\Samuellllll\Descargas\\1S2023LFPB--origin\\1S2023LFPB--origin\\CLASE08\\entrada.txt", "r") as lineas:
    contenido = lineas.read()



class master:

    def __init__(self, entrada:str): 
        self.lineas = entrada
        self.index = 0
        self.fila = 1
        self.columna = 0


    

    def _compilador(self):
        estado_actual = "S0"

        while self.lineas[self.index] != None:
            print(f"CARACTER: {self.lineas[self.index]}  | ESTADO: {estado_actual}  | FILA: {self.fila}  | COLUMNA: {self.columna}")
            
            # INCREMENTA LA LINEA RECONOCIENDO EL SALTO DE LINEA
            if self.lineas[self.index] == "\n":
                self.fila += 1

            
            # ESTADOS

            # S0 -> { S1
            elif estado_actual == "S0":
                estado_actual = self._token('{', "S0", "S1" )

            # S1 -> "Operacion" S2
            elif estado_actual == "S1":
                estado_actual = self._token('"Operacion"', "S1", "S2" )

            elif estado_actual == "S2":
                estado_actual = self._token(':', "S2", "S3" )

            # S3 -> OPERADOR S4
            elif estado_actual == "S3":
                operadores = ['"Suma"', '"Resta"', '"Multiplicacion"', '"Divison"']
                estado_actual = self._token('"Suma"', 'S3', 'S4')

            # S4 -> "Valor1" S5
            elif estado_actual == "S4":
                estado_actual = self._token('"Valor1"', 'S4', 'S5')

            # S5 -> : S6
            elif estado_actual == "S5":
                estado_actual = self._token(':', 'S5', 'S6')



            # INCREMENTA EL INDEX O LA POSICION DEL TEXTO
            if self.index < len(self.lineas) - 1:
                self.index += 1

            else:
                break

    def _analizar(self, token, texto):
        try:
            contador = 0
            token_temp = 0

            for i in texto:
                print('COMBINACION -> ',i , '==', token[contador])
                if str(i) == str(token[contador]):
                    token_temp += 1
                    contador += 1

                else:
                    #print('ERROR1')
                    return False
        
            print(f'********** ENCONTRE: {token_temp} ***************')
            return True
        
        except:
            return False





    def _token(self, token, estado_actual, estado_siguiente):
        if self.lineas[self.index] != " ":
            text = self._combinar(self.index, len(token))
            print("JUNTADO: ", text)

            if self._analizar(token, text):
                self.index += len(token)-1
                return estado_siguiente
            
            else:
                return "ERROR"
        else: 
            return estado_actual
        


    def _combinar(self, indice, contador):
        try:
            tmp = ''
            for i in range(indice, indice + contador):
                tmp += self.lineas[i]

            return tmp
        except:
            return None



analizar = master(contenido)
analizar._compilador()

