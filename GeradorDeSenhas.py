# gerador de senhas

import random
import string


def beginning():
    print('\t ==GERADOR DE SENHAS==')


def senha():
    escolhas_possiveis = string.ascii_lowercase + string.ascii_uppercase + string.digits
    resultado = ''
    for i in range(12):
        resultado += random.choice(escolhas_possiveis)
    print(f'a senha gerada é {resultado}')


beginning()
senha()
