def inicio():
    print('\t ==CONTADOR DE PALAVRAS==')


def ler_palavras():
    frase = str(input('Digite a frase que quer contabilizar o numero de palavras: '))
    palavras = frase.split()
    return palavras

def contador_palavras(palavras):
    contador = len(palavras)
    print(f'o numero de palavras é {contador}')


inicio()
palavras = ler_palavras()
contador_palavras(palavras)
