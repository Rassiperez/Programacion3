def escoger_juego():
    import ahorcado
    import adivinanza

    print('========================================')
    print('Elija su Juego')
    print('========================================')

    print(" (1) Horca  (2) Adivinanza")

    juego = int(input("¿Cuál juego?"))

    if (juego == 1):
        print("Jugando ahorcado")
        ahorcado.jugar()
    elif (juego == 2):
        print("Jugando adivinanza")
        adivinanza.jugar()
       
if(_name_ == "_main_"):
    escoger_juego()