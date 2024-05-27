# calculadora simples com operacoes basicas

def menuInicial():
    print('\tCalculadora simples')
    print('Escolha uma operacao: ')
    print('1) Soma\n2) Subtracao\n3) Multiplicacao\n4) Divisao\n5) Exponenciacao')

def soma():
    n1 = float(input('n1 = '))
    n2 = float(input('n2 = '))
    sum = n1 + n2
    print(f'{n1} + {n2} = {sum}')

def sub():
    n1 = float(input('n1 = '))
    n2 = float(input('n2 = '))
    subtracao = n1 - n2
    print(f'{n1} - {n2} = {subtracao}')

def mult():
    n1 = float(input('n1 = '))
    n2 = float(input('n2 = '))
    multiplicacao = n1 * n2
    print(f'{n1} * {n2} = {multiplicacao}')

def divisao():
    n1 = float(input('n1 = '))
    n2 = float(input('n2 = '))
    divi = n1 / n2
    print(f'{n1} / {n2} = {divi}')

def expo():
    n1 = float(input('n1 = '))
    n2 = float(input('n2 = '))
    exponencicacao = n1 ** n2
    print(f'{n1} ^ {n2} = {exponencicacao}')
def optionsMenu():
    options = int(input('operacao = '))

    match options:
        case 1:
            soma()
        case 2:
            sub()
        case 3:
            mult()
        case 4:
            divisao()
        case 5:
            expo()


menuInicial()
optionsMenu()





