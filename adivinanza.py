def jugar():
    import random
    print('=================================')
    print('Bienvenido al Juego de Adivinanza')
    print('=================================')
    
    numero_secreto = random.randrange(1,101)
    puntaje = 1000     # puntos asignados
    print('Seleccione el nivel de dificultad'  , numero_secreto )
    print('(1) Fácil  (2) Medio (3) Difícil')

    nivel = int(input('Ingrese nivel de dificultad: '))
    if(nivel == 1):
     total_intentos = 20
    elif(nivel == 2):
     total_intentos = 10
    else:
     total_intentos = 5
    for iteracion in range(1, total_intentos +1):
     print('Intento: {} de {} '.format(iteracion,total_intentos))
     entrada = input('Digite un número entre 1 y 100: ')
     entrada= int(entrada)
     print('Digitaste ...', entrada)
     if(entrada<1 or entrada >100):
        print('Ingresar un número entre 1 y 100: ')
        continue
        
     acertaste = entrada == numero_secreto  # iguales
     mayor = entrada > numero_secreto      # entrada es MAYOR
     menor = entrada < numero_secreto      # entrada es MENOR
    
     if(acertaste):
            print('Felicitaciones !!! ... adivinaste el número y ganaste {} puntos'.format(puntaje))
            break
     elif(mayor):
        print('Lo siento ... el número que ingresaste es mayor que el número secreto')
     else:
        print('Lo siento ... el número que ingresaste es menor que el número secreto')

     puntos_perdidos = abs(numero_secreto - entrada)
     puntaje = puntaje - puntos_perdidos
        
    print('Fin del Juego')

if(_name_ == "_main_"):
    jugar()