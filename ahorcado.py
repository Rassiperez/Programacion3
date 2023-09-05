def jugar():
    print('========================================')
    print('Bienvenido al Juego de la horca')
    print('========================================')

    palabra_secreta = 'mandarina'
    letras_acertadas =['','','','','','','','','_']
    
    ahorcado = False
    acerto = False
    
    print(letras_acertadas)
    while(not ahorcado and not acerto):
        entrada= input('Ingrese una letra... ')
        entrada = entrada.strip()
        entrada = entrada.lower()
        indice = 0
        for letra in palabra_secreta:
            if(entrada==letra):
                letras_acertadas[indice] = letra
                #print('Se encontró la letra {} en la posición {}'.format(letra, indice))
                
            indice = indice + 1
        print(letras_acertadas)
        print('jugando... ')
        
        
    print('FIN DEL JUEGO')
    
if(__name__ == "__main__"):
    jugar()