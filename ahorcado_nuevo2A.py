import random as rnd
import os
import juegos as j

def mensaje_ganador():
    print("\n Felicitaciones, ganaste el juego!")
    print("       _____      ")
    print("      '.=====.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         .' '.        ")
    print("        '-------'       ")        
       
    
def mensaje_perdedor(palabra_secreta):
    linea()
    print("\t\t\tPerdiste el Juego")
    linea()
    print("\n Lo siento, fuiste ahorcado!")
    print("La palabra era {}".format(palabra_secreta))
    print("    _____         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \_      XXX      _/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \___/           ")       
    
    
def dibujar_ahorcado(errores, lista,palabraSecreta):
    valor=round(porcentaje_Error(palabraSecreta)*errores)
    print(valor)
    
    print("  ________")
    print(" |/      |    ")

    if(valor == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(valor == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(valor == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(valor == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(valor == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(valor == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (valor == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print(" |__         ")
    linea()
    print(lista)

    
def linea():
    print("========================================================")
    
def porcentaje_Error(palabraSecreta):
    porcentaje=7/len(palabraSecreta)
    return porcentaje

def validar_Letras():
    isLetter=False
    while isLetter==False:
        variable=input("Ingrese letra: ")
        if(len(variable)==1):
            if variable.isalpha():
                isLetter=True
            else:
                print("La entrada debe ser una letra.")
        else:
            print("La entrada debe ser una sola letra.")
    return variable.lower()

def inicio():
    linea()
    print("\t\t\tAhorcado")
    linea()
    respuesta=""
    print("Listo para jugar? S/N")
    while(respuesta != "s" and respuesta != "n"):
        respuesta = validar_Letras()
    if(respuesta=="n"):
        os.system("cls")
        j.escoger_juego()
        
def palabra_Secreta():
    palabras=[]
    f = open("palabras.txt","r")
    for line in f:
        palabra=line.strip()
        palabras.append(palabra)
    f.close()
    palabraSecreta=rnd.choice(palabras)
    return palabraSecreta

def crear_Lista(palabraSecreta):
    return ["-" for letra in palabraSecreta]

def marcar_Correcto(entrada, palabraSecreta, lista):
    encontrada=False
    for i, letra in enumerate(palabraSecreta):
            if(entrada==letra and entrada not in lista):
                lista[i]=letra
                encontrada=True
    return encontrada

def jugar():
    inicio()
    os.system("cls")
    palabraSecreta="chirimoya"
    lista=crear_Lista(palabraSecreta)
    maxErrores=len(palabraSecreta)
    ahorcado=False
    acerto=False
    while(not ahorcado and not acerto):
        print(palabraSecreta)
        dibujar_ahorcado(maxErrores, lista,palabraSecreta)
        entrada=validar_Letras()
        encontrada=marcar_Correcto(entrada, palabraSecreta, lista)
        if(encontrada==False):
            maxErrores-=1
        #print(maxErrores)
        if (maxErrores==0):
            dibujar_ahorcado(maxErrores,lista,palabraSecreta)
            ahorcado=True
            mensaje_perdedor(palabraSecreta)
        if all([i == j for i, j in zip(lista, palabraSecreta)]):
            acerto=True
            mensaje_ganador()
    linea()
    print("\t\t\tFin del Juego")
    linea()
if(__name__=="__main__"):
    jugar()