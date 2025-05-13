
saida = ''


def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

def calculadora(n1, n2, op):
    op = op.strip().lower()
    resultado = None
    
    if op in ['+', 'adicao', 'soma']:
        resultado = adicao(n1, n2)
    elif op in ['-', 'subtracao', 'subtração']:
        resultado = subtracao(n1, n2)
    elif op in ['*', 'multiplicacao', 'multiplicação', 'x']:
        resultado = multiplicacao(n1, n2)
    elif op in ['/', 'divisao', 'divisão']:
        resultado = divisao(n1,  n2)
    else:
        resultado = 'Operação desconhecida'
    return resultado


while saida.lower() != 'n':
    
    n1 = float(input("Digite o primeiro número: "))
    
    n2 = float(input("Digite o segundo número: "))
   
    op = input("Digite a operação (+, -, *, /) ou o nome da operação: ")
    
    
    resultado = calculadora(n1, n2, op)
    print("Resultado da operação:", resultado)
    
    
    saida = input("Deseja continuar? (S/N): ")

print("Programa encerrado.")