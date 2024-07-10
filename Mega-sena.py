import random

numeros_sorteados = random.sample(range(1, 61), 6)

numeros_usuario = input("Digite os números de sua cartela: ")
numeros_usuario = list(map(int, numeros_usuario.split()))

while len(numeros_usuario) != 6 or len(set(numeros_usuario)) != 6 or any(numero < 1 or numero > 60 for numero in numeros_usuario):
    numeros_usuario = input("Entrada inválida!, Tente novamente:  ")
    numeros_usuario = list(map(int, numeros_usuario.split()))

numeros_corretos = set(numeros_usuario) & set(numeros_sorteados)
print("Números sorteados:", numeros_sorteados)
print("Seus números:", numeros_usuario)
print("Você acertou", len(numeros_corretos), "número(s)!")
