import random

chances = 9


def inicio():
    print('\t ==JOGO DE ADIVINHACAO==')


def advinhe(chances):
    chances_restantes = chances
    num_aleatorio = random.randint(1, 50)

    escolha1 = int(input('Um número entre 1 e 50 foi escolhido aleatoriamente. Tente adivinhar: '))
    tentativas_jogador.append(escolha1)

    while chances_restantes > 0:
        print(f'voce escolheu o numero {escolha1}')
        print('Escolha errada. tente novamente.')
        print(f'voce tem {chances_restantes} chances restantes.\n')
        escolha = int(input('digite um numero entre 1 e 50: '))

        chances_restantes -= 1

        tentativas_jogador.append(escolha)

        if escolha < 0 or escolha > 50:
            print('fora do intervalo. tente novamente.')
            continue

        if escolha == num_aleatorio:
            print(f'voce escolheu o numero {escolha} ')
            print('voce acertou. Parabens!')
            break
        elif escolha < num_aleatorio:
            print(f'o numero {escolha} é menor que o numero da adivinhacao')
        else:
            print(f'o numero {escolha} é maior que o numero de adivinhacao')

        if chances_restantes == 0:
            print('as chances acabaram.')

    return tentativas_jogador


def exibir_tentativas(tentativas_jogador):
    print('\t ==HISTORICO DE TENTATIVAS==')
    for i, tentativa in enumerate(tentativas_jogador):
        print(f'{i + 1}: {tentativa}')


inicio()
tentativas_jogador = []
advinhe(chances)
exibir_tentativas(tentativas_jogador)
