#================================================
#=== Anna Carolina de Oliveira Vale Mendes - PROF: MASSANORI ====
#================================================

'''' Quarta lista de exercícios'''

z="s"
while z=="s":
    r=int(input("Selecione os exercícios da 'Lista IV - De Python - Professor Massanori - FATEC - SJC', selecione o exercício que deseja ver, de (1 a 5): "))
    print ("Digite s, quando quiser sair")
    print ("Anna Carolina de Oliveira Vale Mendes - 17/05/2020.")
    
    if r == 1:
        print('1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.')
        print("Resolução abaixo:")

        from random import randint
        vetor = []
        for k in range(10):
            vetor.append(randint(1, 100))
            
        maior = menor = vetor[0]

        k = 1
        while k < 10:
            if vetor[k] > maior:
              maior = vetor[k]
            if vetor[k] < menor:
              menor = vetor[k]
            k = k + 1

        print ('Vetor:', vetor)
        print ('Maior: %d' %maior)
        print ('Menor: %d' %menor)

    elif r == 2:
         print('2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.')
         print("Resolução abaixo:")

         import random
         vetor = []
         for k in range(20):
             vetor.append(random.randint(1, 100))

         pares = []
         ímpares = []

         for x in vetor:
             if x % 2 == 0:
                 pares.append(x)
             else:
                 ímpares.append(x)
         print ('Vetor', vetor)
         print ('Pares', pares)
         print ('Ímpares', ímpares)

    elif r == 3:
         print('3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.')
         print("Resolução abaixo:")

         from random import randint
         v1 = []
         v2 = []
         v3 = []

         for k in range(10):
             x = randint(1, 100)
             v1.append(x)
             v3.append(x)
             x = randint(1, 100)
             v2.append(x)
             v3.append(x)
         print('v1:', v1)
         print('v2:', v2)
         print('v3:', v3)

    elif r == 4:
        print('4. Seja o statement sobre diversidade: “The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas. ')
        print("Resolução abaixo:")

        texto = '''The Python Software Foundation and the global
   Python community  welcome and encourage participation
   by everyone. Our community is based on mutual respect,
   tolerance, and encouragement, and we are working to
   help each other live up to these principles. We want
   our community to be more diverse: whoever you are, and
   whatever your background, we welcome you.'''.lower()

        # google > psf diversity statement
        import string
        for c in string.punctuation:
            texto = texto.replace(c, ' ')
            
        resp = []
        for p in texto.split():
            if p[0] in 'python' or p[-1] in 'python':
                resp.append(p)
        print (resp)

    elif r == 5:
        print('5. Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.')
        print("Resolução abaixo:")

        texto = '''The Python Software Foundation and the global
   Python community  welcome and encourage participation
   by everyone. Our community is based on mutual respect,
   tolerance, and encouragement, and we are working to
   help each other live up to these principles. We want
   our community to be more diverse: whoever you are, and
   whatever your background, we welcome you.'''.lower()

        import string
        for c in string.punctuation:
            texto = texto.replace(c, ' ')

        def pitônica(palavra):
            for letra in palavra:
                if letra in 'python':
                    return True
            return False

        resp = []
        for p in texto.split():
            if pitônica(p) and len(p) > 4:
                resp.append(p)
        print (resp)
        print (len(resp))

    else:
        print("Finalizado (1 a 5)")
        r !="s"
        break       
