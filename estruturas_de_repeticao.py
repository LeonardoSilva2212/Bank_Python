# Percorrendo uma lista
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

#----------------#

#While

# Repetindo enquanto a condição for verdadeira
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

#----------------#

#Break e continue

# Usando break para interromper um loop
for i in range(10):
    if i == 5:
        break  # Sai do loop quando i é 5
    print(i)

# Usando continue para pular uma iteração
for i in range(10):
    if i % 2 == 0:
        continue  # Pula os números pares
    print(i)

#----------------#

# For com else

# else em um for
for numero in range(5):
    print(numero)
else:
    print("Loop concluído com sucesso!")

#----------------#

# While com else

# else em um while
x = 0

while x < 5:
    print(x)
    x += 1
else:
    print("While concluído com sucesso!")

#----------------#

