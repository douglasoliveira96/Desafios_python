#Programa que lê valor em metro e exibe convertido em centímetros e milímetros
m = int(input('Metros: '))
cm = m*100
mm = m*1000
print('{} metros é igual a {} centímetros \nou {} milímetros.'.format(m, cm, mm))