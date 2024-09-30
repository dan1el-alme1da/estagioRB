
texto = input("Digite uma string: ")


contador = 0


for caractere in texto:
    if caractere.lower() == 'a':
        contador += 1


if contador > 0:
    print(f"A letra 'a' aparece {contador} vezes na string.")
else:
    print("A letra 'a' não foi encontrada na string.")
