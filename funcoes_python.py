def exibir_mensagem():
    print("Olá Mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Leo")
exibir_mensagem_3()
exibir_mensagem_3(nome="Douglas")

def calcular_total(numeros):
    return sum (numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10)) 