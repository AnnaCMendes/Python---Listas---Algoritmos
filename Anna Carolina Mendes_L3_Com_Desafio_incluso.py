#================================================
#=== Anna Carolina de Oliveira Vale Mendes - 1B PROF: MASSANORI - 2020 ====
#================================================

'''' Terceira lista de exercicios/ lembrando que o Desafio se encontra nessa lista - Desafio são númerdos de 6 à 10, contando que essa lista, está numera de 1 à 5, a sequência 6=1 e assim, segue a sequência'''

z="s"
while z=="s":
    r=int(input("Selecione os exercícios da 'Lista III e LISTA III(Desafio (Desafio númerados de 6 à 10, considerando que essa sequência é como se fosse de 1 à 5, como representado em lista.))- De Python - Professor Massanori - FATEC - SJC',selecione o exercício que deseja ver, de (1 a 10): "))
    print ("Digite s, quando quiser sair")
    print ("Eu sou feliz, gosto de programar. Anna Carolina de Oliveira Vale Mendes - 30/08/2019.")

    if r == 1:
        print('1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.')
        print("Resolução abaixo:")

        nota=float(input("Digite Nota entre (0 a 10): "))

        while nota <0 or nota >10:
            print("Nota entre (0 a 10): ")
            nota=float(input("Digite Nota entre (0 a 10): "))

    elif r == 2:
        print("2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.")
        print(" Resolução abaixo:")

        nome=input("Digite Usuário: ")
        senha=input("Digite senha do Usuário: ")

        while nome == senha:
            print("Senha igual ao Usuário, digite senha diferente de Usuário")
            nome=input("Digite Usuário: ")
            senha=input("Digite senha do Usuário: ")

    elif r == 3:
        print("3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento")
        print("Resolução abaixo:")

        a = 80000
        b = 200000
        anos = 0

        while a <= b:
            a = a + a * 0.03
            b = b + b * 0.015
            anos = anos + 1
        print(anos)

    elif r == 4:
        print("4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.")
        print("Resolução abaixo")

        n = int(input('Digite o valor de n: '))

        a, b = 1, 1
        k = 1

        while k <= n - 2:
            a, b = b, a + b
            k = k + 1

        print(b)

    elif r == 5:
        print("5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides. ")
        a = int(input('Valor de a: '))
        b = int(input('Valor de b: '))

        while a % b != 0:
            a, b = b, a % b
        print('mdc = %d' % b)

    elif r==6:
        print ("6. Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular. ")

        n = int(input('N: '))
        k = 0
        while k * (k + 1) * (k + 2) < n:
            k = k + 1

        print (k * (k + 1) * (k + 2) == n)

    elif r==7:
        print ("7. Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.")
        conta = int(input('Conta: '))
        pgto = int(input('Pagamento: '))
        troco = pgto - conta
        notas = [50, 20, 10, 5, 2, 1]
        for nota in notas:
            while troco >= nota:
                print ('Uma nota de %d' %nota)
                troco -= nota
    
    elif r==8:
        print ("8.Verifique se um inteiro positivo n é primo.")
        num=int(input("Numero:"))
        if num%2==1:
            print("primo")
        else:
            print ("não é primo")

    elif r==9:
        print ("9.Dado um número inteiro positivo, determine a sua decomposição em fatores primos calculando também a multiplicidade de cada fator.")
        n = int(input('Número: '))
        for k in range(2, n):
          while n % k == 0:
            print (k)
            n = n / k


    elif r==10:
        print ("10. Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321")
        n = int(input('Número: '))
        inv = 0
        while n > 0:
            inv *= 10
            inv += n % 10
            n //= 10
            print(inv)


    else:
        r !="s"
        break

        




