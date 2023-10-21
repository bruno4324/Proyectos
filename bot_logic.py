import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
x = int(input("Cuantas letras tendrá:"))
for i in range(x):
    letra = random.choice(caracteres)
    print(letra)
