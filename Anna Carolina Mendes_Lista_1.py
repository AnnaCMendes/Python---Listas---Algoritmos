'''Exercicios da Anna Carolina de Oliveira Vale Mendes, segue todos em sequencia - 2020'''

# 1- Faça um programa que peça dois números inteiros e imprima a soma desses dois números.

num1=int(input("Digite o 1 número: "))
num2=int(input("Digite o 2 número: "))

print(num1+num2)

# 2- Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

num=int(input("Digite um valor em Metros: "))

print(" Em Milímetros:", num*1000)

# 3 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias=int(input("Quantos dias: "))
horas=int(input("Quantas horas: "))
minutos=int(input("Quantos minutos: "))
segundos=int(input("Quantos segundos: "))

total=(dias*24*60*60+horas*60*60+minutos*60+segundos)

print(total)

# 4- Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário
# e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

sal=float(input("Digite o valor do Salário atual: "))
por=float(input("Digite a Porcentagem de aumento: "))
aumento=sal*(por/100)
novosal=(sal+aumento)
print("Aumento de: R$ %.2f" %aumento)
print("Novo Salário é: R$ %.2f" %novosal)

# 5 - Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preço=float(input("Qual o valor da mercadoria: "))
perc=float(input("Qual o valor de desconto: "))

desconto=(preço*(perc/100))
novopreço=(preço-desconto)

print("Valor do Desconto: R$ %.2f" %desconto)
print("Preço final de: R$ %.2f" %novopreço)


# 6 - Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia=float(input("Distância percorrida em KM: "))
velocidade=float(input("Velocidade média em KM/H: "))

tempo=(distancia/velocidade)

print("Tempo total da viagem em horas: %.1f" %tempo)

# 7 - Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

c=float(input("Digite a Temperatura em graus Celsius: "))

f=9*c/5+32

print=("%.2f Fahrenheit" %f)

# 8 - Faça agora o contrário, de Fahrenheit para Celsius.

f=float(input("Digite temperatura em Fahrenheit: "))

c=(f-32)*5/9

print("%.2f Celcios" %c)

# 9 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

perc=float(input("Qual a KM percorrida: "))
dias=int(input("Quantos dias em uso: "))

preço=(60*dias+0.15*perc)

print("R$: %.2f" %preço)

# 10 - Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

''' (1 dia = 1440 minutos = 144 cigarros) '''


cigarros=int(input("Quantos cigarros por dia: "))
anos=int(input("Quantos anos você fuma: "))

totalcigarros=(anos*365*cigarros)
totalperdido=(totalcigarros/144)

print("Você perdeu aproximadamente %.2f dias de vida" %totalperdido)

# 11 - Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

print (len(str(2**1000000)))



