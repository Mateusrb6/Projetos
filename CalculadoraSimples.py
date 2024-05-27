# calculadora simples com operacoes basicas

def menu():
    print('\tCalculadora simples')
    print('Escolha uma operacao: \n')
    print('1) Soma\n2) Subtracao\n3) Multiplicacao\n4)Divisao\n5) Exponenciacao')

def soma():
    n1 = float(input('n1 = '))
    n2 = float(input('n2 = '))
    sum = n1 + n2
    return sum

def sub():
    n1 = float(input('n1 = '))
    n2 = float(input('n2 = '))
    subtracao = n1 - n2
    return subtracao

def mult():
    n1 = float(input('n1 = '))
    n2 = float(input('n2 = '))
    multiplicacao = n1 * n2
    return multiplicacao

def divisao():
    n1 = float(input('n1 = '))
    n2 = float(input('n2 = '))
    divi = n1 / n2
    return divi
def optionsMenu():
    options = int(input('operacao = '))
    while True:
        match options:
            case 1:
                soma()
            case 2:
                sub()
            case 3:
                mult()
            case 4:
                divisao()







menu()
optionsMenu()





