# Função para inverter uma string
def inverter_string(s):
    string_invertida = ""
    # percorre a string do último caractere até o primeiro
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# Exemplo de string a ser invertida
string_original = input("Digite uma string para inverter: ")

# Invertendo a string
resultado = inverter_string(string_original)

# Exibindo o resultado
print("String invertida:", resultado)
