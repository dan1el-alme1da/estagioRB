def é_fibonacci(n):
    def quadrado_perfeito(x):
        s = int(x ** 0.5)
        return s * s == x
    
   
    return quadrado_perfeito(5 * n * n + 4) or quadrado_perfeito(5 * n * n - 4)


numero = int(input("Digite um número: "))


if é_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")