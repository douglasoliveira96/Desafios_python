#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#desconsiderando os espaços.
frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('\033[1mA frase "{}" \033[1;34mÉ UM PALINDROMO.\033[m'.format(frase))
else:
    print('\033[1mA frase "{}" \033[1;31mNÃO É UM PALINDROMO.\033[m'.format(frase))