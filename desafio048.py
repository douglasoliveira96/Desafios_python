#Faça um programa que calcule a soma entre todos os números
#que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for num in range(1, 501, 2):
        if num % 3 == 0:
            soma += num
            cont += 1
print('A soma entre os {} valores solicitados é \033[1m{}.\033[m'.format(cont, soma))
