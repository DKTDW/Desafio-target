def pertence_fibonacci(n):
    # Inicializa a sequência de Fibonacci
    fibonacci = [0, 1]
    
    # Gera a sequência de Fibonacci até o número informado
    while fibonacci[-1] < n:
        proximo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo)

    # Verifica se o número pertence à sequência
    if n in fibonacci:
        return True
    else:
        return False

# Solicita ao usuário para informar um número
numero = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
