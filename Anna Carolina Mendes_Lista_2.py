'''Exercicios da Anna Carolina de Oliveira Vale Mendes, segue todos em sequencia -  2020 '''

# 1 - Faça um Programa que peça os três lados de um triângulo. O programa deverá informar
# se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
# se o mesmo é: equilátero, isósceles ou escaleno.

a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))
if a > b + c or b > a + c or c > a + b:
  print ('Não pode ser um triângulo')
  print ('Um dos lados é maior que a soma dos outros')
elif a == b == c:
  print ('Equilátero')
elif a == b or b == c or a == c:
  print ('Isósceles')
else:
  print ('Escaleno')

  
# 2- Determine se um ano é bissexto. Verifique no Google como fazer isso...

a = int(input('Ano: '))
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
  print ('Bissexto')
else:
  print ('Não é bissexto')


# 3 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.     
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca
# do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso.
# Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar.
# Caso contrário mostrar tais variáveis com o conteúdo ZERO.

peso = float(input('Peso: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    multa = excesso = 0

print ('Multa de R$ %.2f' %multa)
print ('Excesso: %.2f' %excesso)


# 4 - Faça um Programa que leia três números e mostre o maior deles

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a >= b and a >= c:
    print ('Maior: %d' %a)
elif b >= c:
    print ('Maior: %d' %b)
else:
    print ('Maior: %d' %c)


# 5 - Faça um Programa que leia três números e mostre o maior e o menor deles.

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a >= b and a >= c:
    print ('Maior: %d' %a)
elif b >= c:
    print ('Maior: %d' %b)
else:
    print ('Maior: %d' %c)

if a <= b and a <= c:
    print ('Menor: %d' %a)
elif b <= c:
    print ('Menor: %d' %b)
else:
    print ('Menor: %d' %c)


# 6 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.     
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou
# ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido.
# Calcule os descontos e o salário líquido, conforme a tabela abaixo:

# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato ( 5%) : R$
# e. = Salário Liquido : R$

valor = float(input('Valor por hora: '))
horas = int(input('Horas tralhadas: '))
bruto = valor * horas
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - ir - inss - sind
print ('+Salário Bruto:\t\t R$ %10.2f' %bruto)
print ('-IR:\t\t\t R$ %10.2f' %ir)
print ('-INSS:\t\t\t R$ %10.2f' %inss)
print ('-Sindicato:\t\t R$ %10.2f' %sind)
print ('=Salário Líquido:\t R$ %10.2f' %liquido)


# 7 - Faça um programa para uma loja de tintas.     
# O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura
# da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
# é vendida em latas de 18 litros, que custam R$ 80,00
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# Obs. : somente são vendidos um número inteiro de latas.

m = int(input('Metros: '))
if m % 54 == 0:
  latas = m / 54
else:
  latas = int(m / 54) + 1

valor = latas * 80
print ('%d latas' %latas)
print ('Total: R$ %.2f' %valor)
