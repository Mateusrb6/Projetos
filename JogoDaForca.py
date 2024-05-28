#Jogo da Forca
import random

letras_usuario = []
chances = 7
ganhou = False


def inicio():
    print('\t== JOGO DA FORCA ==\n')


def escolher_palavra():
    palavras = ["abacaxi", "melancia", "banana", "morango"]
    return random.choice(palavras)


def mostrar_palavra(palavra, letras_usuario):
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("")


def verificar_ganho(palavra, letras_usuario):
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            return False
    return True


def jogo_da_forca():
    inicio()
    palavra = escolher_palavra()
    letras_usuario = []
    chances = 7
    ganhou = False

    while True:
        mostrar_palavra(palavra, letras_usuario)
        print(f'Chances restantes: {chances}')
        tentativa = input('Escolha uma letra: ').lower()

        if tentativa in letras_usuario:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_usuario.append(tentativa)

        if tentativa not in palavra:
            chances -= 1
            print(f'Letra incorreta! Você perdeu uma chance.')

        ganhou = verificar_ganho(palavra, letras_usuario)

        if chances == 0 or ganhou:
            break

    if ganhou:
        print(f'Parabéns, você ganhou! A palavra era: {palavra}')
    else:
        print(f'Você perdeu! A palavra era: {palavra}')


# Iniciar o jogo
jogo_da_forca()
