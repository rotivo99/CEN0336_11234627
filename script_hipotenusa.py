#!/usr/bin/env python3

import sys

#Criando variáveis para armazenar os valores inseridos pelo usuário. Está sem o int porque não dá para usar o isdigit() com inteiros.
value_1 = sys.argv[1]
value_2 = sys.argv[2]

if value_1.isdigit() and value_2.isdigit(): #Se ambos os valores inseridos forem digitos, haverá uma mensagem confirmatória e o código continuará rodando.
    print('Ambos os valores inseridos são digitos. Prosseguindo...')
else: #Se não forem, haverá uma mensagem pedindo por valores válidos...
    print('Algum ou ambos os valores inseridos não são digitos ou inteiros. Insira valores válidos.')
    sys.exit() #...e então o código para para que eles sejam inseridos.

#As mesmas variáveis de antes, mas agora elas precisam ser números inteiros porque serão comparadas com os valores das condições.
value_1 = int(sys.argv[1])
value_2 = int(sys.argv[2])

if value_1 and value_2 > 0 and value_1 and value_2 < 500: #Se os números inseridos estiverem dentro do intervalo determinado...
    hipotenusa = value_1**2 + value_2**2 #...eles cairão nessa equação...
    saida = 'O quadrado da hipotenusa para o triângulo retângulo de lados a = {} e b = {} é {}.' #...e essa saída será exibida.
    print(saida.format(value_1, value_2, hipotenusa)) #Aqui encontra-se a saída formatada.
else: #Caso os números estejam fora do intervalo...
    print('Algum ou ambos os valores inseridos estão fora do limite de 1 a 499.') #...uma mensagem pedindo por valores dentro do intervalo será exibida.
