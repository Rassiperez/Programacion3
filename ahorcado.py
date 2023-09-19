import random
def jugar():
    print('========================================')
    print('Bienvenido al Juego de la horca')
    print('========================================')

    archivo= open('palabras.txt', 'r')
    palabras = [] 
    for linea in archivo:
        linea= linea.strip()
        palabras.append(linea)
        
    archivo.close()
    numero = random.randrange(0, len(palabras))
    
    
    palabra_secreta = palabras[numero].lower()
    letras_acertadas =['_' for elemento in palabra_secreta]
    
    ahorcado = False
    acerto = False
    errores = 0 #contador de errores
    
    print(letras_acertadas)
    while(not ahorcado and not acerto):
        entrada= input('Ingrese una letra... ')
        entrada = entrada.strip()
        entrada = entrada.lower()
        
        if entrada in palabra_secreta:
            indice = 0
            for letra in palabra_secreta:
                if(entrada==letra):
                    letras_acertadas[indice] = letra
                    #print('Se encontró la letra {} en la posición {}'.format(letra, indice))

                indice = indice + 1
        else:
            errores += 1
            
        ahorcado = errores == 9
        acerto = "_" not in letras_acertadas
        print(letras_acertadas)
       
    if(acerto):
        print('¡¡¡Felicidades, ganaste!!!')
    else:
        print('Lo siento, perdiste...')
       
    print('FIN DEL JUEGO')
    
if(__name__ == "__main__"):
    jugar()