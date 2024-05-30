# numero de faces, quantas vezes rolar e exibir resultados
import random


def inicio():
    print('\t ==ROLAGEM DE DADOS==')
    print('1. Defina o numero de faces do dado. ')
    print('2. Defina quantas vezes deseja rolar o dado. ')


def opcoes():
    faces = int(input('numero de faces: '))
    quantidade_rolagens = int(input('numero de rolagens: '))
    return faces, quantidade_rolagens

def rolagem(faces, quantidade_rolagens):
    for i in range(quantidade_rolagens):
        rodada = random.randint(1, faces)
        print(f'o numero da rodada {i+1} foi {rodada}')

def jogo():
    inicio()
    faces, quantidade_rolagens = opcoes()

    rolagem(faces, quantidade_rolagens)

jogo()
