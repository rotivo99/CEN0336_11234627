#!/usr/bin/env python3

import sys

#Criando variáveis para armazenar os valores inseridos pelo usuário. Está sem o int() porque não dá para usar o isalpha() nem o isdigit() com inteiros.
dna = sys.argv[1].upper() #O upper() para que não haja problemas em lidar com entradas em que as letras estão minúsculas, porque nos métodos de busca que serão utilizados mais tarde, as strings estão em maiúsculo.
n1 = sys.argv[2]
n2 = sys.argv[3]
n3 = sys.argv[4]
n4 = sys.argv[5]

#Checando se a string inserida em dna é constituída exclusivamente de letras.
if dna.isalpha(): #Se verdadeiro...
    print('A sequência inserida é válida. Prosseguindo...') #...o código segue em frente.
else: #Se falso...
    print('A sequência inserida deve conter exclusivamente letras. Insira uma sequência de DNA válida.') #...o usuário tem que reinserir os valores...
    sys.exit() #...e para que isso aconteça, o código para.

#Checando se as informações inseridas em n1-4 são números inteiros.
if n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit():
    print('Os números inseridos são válidos. Prosseguindo...')
else:
    print('Os dados inseridos não são números ou, se são, não são inteiros. Insira valores válidos.')
    sys.exit()

#Medindo o tamanho da sequência atribuída à dna. Será utilizada no próximo bloco.
length_dna = len(dna)

#As mesmas variáveis de antes, mas agora elas precisam ser números inteiros porque serão comparadas com os valores das condições.
n1_int = int(sys.argv[2]) - 1 #Retirando 1 do valor inicial de cada éxon para que o valor inserido pelo usuário seja o mesmo que o utilizado pelo python.
n2_int = int(sys.argv[3]) #Como o valor final não é incluído, ele já vem certo.
n3_int = int(sys.argv[4]) - 1
n4_int = int(sys.argv[5])

if n1_int and n2_int and n3_int and n4_int > 0: #Todos valores inseridos têm que ser maiores que 0...
    if n1_int < n2_int and n3_int < n4_int: #...o valor inicial do éxon tem que ser menor que seu valor final...
        if n1_int and n2_int and n3_int and n4_int < length_dna: #...e todos os valores inseridos têm que ser menores que o tamanho total da sequência.
            print('Os números inseridos estão corretos e dentro do intervalo da sequência. Prosseguindo...')
        else:
            print('Algum dos números inseridos é igual ou maior do que o número de caracteres da sequência. Insira valores válidos.')
            sys.exit()
    else:
        print('O valor inicial de algum ou de ambos os éxons é maior do que o seu valor final. Insira valores válidos.')
        sys.exit()
else:
    print('Algum dos números inseridos é igual ou menor do que 0. Insira valores válidos.')
    sys.exit()

print('')

CDS_1 = dna[n1_int:n2_int] #Isolando o éxon 1 em sua própria variável.
CDS_1_len = len(CDS_1) #Medindo o comprimento do éxon 1.
CDS_2 = dna[n3_int:n4_int] #Isolando o éxon 2 em sua própria variável.
CDS_2_len = len(CDS_2) #Medindo o comprimento do éxon 2.

#Conferindo se o éxon 1 é iniciado por ATG.
if CDS_1.startswith('ATG'):
    print('O códon de início ATG foi encontrado na sequência inserida.')
else:
    print('Não foi encontrado nenhum códon ATG na sequência inserida. Tente outra sequência ou outros valores')
    sys.exit()

#Conferindo se o éxon 2 termina com algum códon de parada.
stop_codons = 'TAG', 'TAA', 'TGA' #Atribuindo os códons a uma variável.
if CDS_2.endswith(stop_codons):
    print('O códon de parada', CDS_2[-3:], 'foi encontrado na sequência inserida.')
else:
    print('Nenhum código de parada foi encontrado na sequência inserida. Tente outra sequência ou outros valores.')
    sys.exit()

print('')

#Unindo os éxons em uma única variável.
concatenate = CDS_1 + CDS_2

#Calculando as posições iniciais e finais de cada éxon.
CDS_1_start = dna.find(CDS_1) + 1 #Corrigindo os valores de saída para que os valores interpretados pelo python sejam os mesmos que os digitados pelo usuário.
CDS_1_end = n2_int
CDS_2_start = dna.find(CDS_2) + 1
CDS_2_end = n4_int

#Organizando os dados obtidos para cada éxon bem como para o mRNA processado.
CDS_1_info = 'O primeiro éxon tem {} nucleotídeos e vai do {}º até o {}º nucleotídeo, tendo a sequência: {}.'.format(CDS_1_len, CDS_1_start, CDS_1_end, CDS_1)
CDS_2_info = 'O segundo éxon tem {} nucleotídeos e vai do {}º até o {}º nucleotídeo, tendo a sequência: {}.'.format(CDS_2_len, CDS_2_start, CDS_2_end, CDS_2)
concatenate_info = 'O mRNA processado tem a seguinte sequência: {}.'.format(concatenate)

#Formatando os dados obtidos para cada éxon bem como para o mRNA processado.
print('{:15}'.format('CDS 1'), CDS_1_info)
print('{:15}'.format('CDS 2'), CDS_2_info)
print('{:15}'.format('mRNA Processado'), concatenate_info)
