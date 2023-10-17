import random 

class Dibujar:
    def dibujar_parte_1(self):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    def dibujar_parte_2(self):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
        
    def dibujar_parte_3(self):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    def dibujar_parte_4(self):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
        
    def dibujar_parte_5(self):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
        
    def dibujar_parte_6(self):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
        
    def dibujar_parte_7(self):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        
        
# Crear una instancia de la clase
d = Dibujar()

def imprimir_mensaje_inicial():
    print('================================')
    print('Bienvenido al Juego del Ahorcado')
    print('================================')

def definir_palabra_secreta():
    archivo = open('palabras.txt', 'r')
    palabras = []
    for linea in archivo:
        linea = linea.strip()
        palabras.append(linea)

    archivo.close()
    numero = random.randrange(0,len(palabras))
    palabra_secreta = palabras[numero].lower()
    return palabra_secreta

def medir_largo_palabra(palabra_secreta):
    return len(palabra_secreta)
    
def inicializar_letras_acertadas(palabra_secreta):
    return ['_' for elemento in palabra_secreta]
    

def leer_entrada():
    entrada = input('Ingrese una letra ...')
    entrada = entrada.strip()                 # elimina espacio en blanco a la izquierda y derecha
    entrada = entrada.lower()                 # convierte a letras minúsculas
    return entrada
    
def marcar_entrada_correcta(entrada, palabra_secreta, letras_acertadas):
    indice = 0
    for letra in palabra_secreta:
        if(entrada==letra):
            letras_acertadas[indice] = letra
        indice = indice + 1    

        
def imprimir_mensaje_ganador():
    print("\n Felicitaciones, ganaste el juego!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")        
       
    
def imprimir_mensaje_perdedor(palabra_secreta):
    print("\n Lo siento, fuiste ahorcado!")
    print("La palabra era {}".format(palabra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")       
    
        
def dibujar_ahorcado(errores,pasos_dibujo, d):
    print("  _______     ")
    print(" |/      |    ")
    
    pasos = pasos_dibujo[errores-1]
    suma_anterior = sum(pasos_dibujo[:errores-1])
    
    getattr(d, f'dibujar_parte_{pasos + suma_anterior}')()     
    
    print(" |            ")
    print("_|___         ")
    print() 
     
    
def calcular_iteraciones_dibujo(largo_palabra, pasos_dibujo):
    # rellenar pasos_dibujo con unos
    for i in range(largo_palabra):
        pasos_dibujo.append(1)  # agregagamos un 1 a la list
    sumar_pasos = sum(pasos_dibujo) # sumamos el contenido de la lista
     
    while(sumar_pasos<7 and largo_palabra < 7):      # cuando la palabra tiene menos de 7 letras
        # ciclo para recorrer pasos_dibujo
        for i in range(largo_palabra):
            pasos_dibujo[i] = pasos_dibujo[i] + 1
            sumar_pasos = sum(pasos_dibujo) # sumamos el contenido de la lista
            if(sumar_pasos == 7):
                break
        


    while(sumar_pasos>7 and largo_palabra > 7):      # cuando la palabra tiene mas de 7 letras
        # ciclo para recorrer pasos_dibujo
        for i in range(largo_palabra):
            if i % 2 != 0:     # detrmina si es impar
                pasos_dibujo[i] = 0
                sumar_pasos = sum(pasos_dibujo) # sumamos el contenido de la lista
            if(sumar_pasos == 7):
                break
    
    return pasos_dibujo # sumar_pasos #pasos_dibujo
    
                                
                                
def jugar():
  
  imprimir_mensaje_inicial()
    
  palabra_secreta = definir_palabra_secreta()

  letras_acertadas =inicializar_letras_acertadas(palabra_secreta)
  
  ahorcado = False
  acerto = False
  errores = 0  # contador de errores
    
  pasos_dibujo = []  # guarda las iteraciones para dibujar ahorcado
  pasos_dibujo = calcular_iteraciones_dibujo(len(palabra_secreta), pasos_dibujo)
  print(pasos_dibujo)
  
  print(letras_acertadas)
  while(not ahorcado and not acerto):
    
    entrada = leer_entrada()
    
    if entrada in palabra_secreta:
        marcar_entrada_correcta(entrada, palabra_secreta, letras_acertadas)
    else:
        errores += 1
        dibujar_ahorcado(errores,pasos_dibujo, d)
    
    ahorcado = errores == medir_largo_palabra(palabra_secreta) # largo de palabra_secreta
    acerto = "_" not in letras_acertadas
    print(letras_acertadas)

  if(acerto):
    imprimir_mensaje_ganador()
  else:
    imprimir_mensaje_perdedor(palabra_secreta)
    
  
    
if(__name__ == "__main__"):
    jugar()
    