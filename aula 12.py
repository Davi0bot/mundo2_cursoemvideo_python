'''
nome = (input('digite seu nome:')).lower()
if nome[:1] == 'a':
    print('que nome lindo')
elif 'k' in nome or 'v' in nome:
    print('que nome estranho')
else:
    print('bem normal')
print('tenha um bom dia {}'.format(nome))
'''
from pandas.io.formats.format import return_docstring

#desafios 1-10
'''
#1 Calculando empréstimo:
valor = int(input('digite o valor da casa:'))
salario = float(input('digite o seu salario:'))
anos = int(input('vai pagar em quantos anos:'))
parcela = valor/12 /anos
if salario * 0.3 >= parcela:
    print('\033[32mEmprestimo aprovado\n\033[m cada parcela sera R${:.2f}'
          'isso é menos de 30% de seu salário'.format(parcela))
else:
    print('\033[31mEmprestimo reprovado\n\033[mcada parcela sera de R${:.2f}'
          'mais de 30% de seu salaário'.format(parcela))
'''
#2 Convertendo para binario, octal ou hexadecimal:
'''
num1 = int(input('digite um numero:'))
a = input('digite b para binario, o para octal e h para hexadecimal').lower()

if a =='b':
    print(bin(num1))
elif a == 'o':
    print(oct(num1))
elif a == 'h':
    print(hex(num1))
else:
        print('inválido')


#3 Comparando 2 numeros:
n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))
if n1 > n2:
    print('o primeiro valor é maior')
elif n1 == n2:
    print('os dois valores sao iguais')
else:
    print('o segundo valor é maior')
'''
#4 Tempo para alistamento:

'''
import datetime
ano_atual = datetime.date.today().year
nasc = int(input('Digite o ano em que voce nasceu:'))
diferença = ano_atual - nasc - 19
diferença_n = diferença + diferença*-2
if ano_atual - nasc > 19:
    print(f'voce ja deveria ter feito o alistamento à {diferença} anos')
if ano_atual - nasc < 19:
    print(f'voce fara o alisatmento daqui {diferença_n} anos')
if ano_atual - nasc == 19:
    print(f'voce deve fazer o alistamento imediatamente')
'''

#5 Média:
'''
def medias():
    while True:
        n1 = int(input('digite a primeira nota:'))
        n2 = int(input('digite a segunda nota:'))

        notas = n1 + n2
        media = (n1 + n2) / 2

        if n1 > 10 or n2 > 10:
            print('invalido')
            continue
        elif media > 7:
            print('aprovado')
        elif media < 6.9 and media >= 5:
            print(('recuperação'))
        else:
            print('reprovado')
        break
medias()
'''
#6 Classificação de categoria/idade:
'''
import datetime
data = datetime.date.today().year
ano = int(input('Digite o ano de seu nascimento:'))
idade = data-ano
categoria = 'indefinido'
if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    cateoria = 'Infantil'
elif idade <= 19:
    categoria = 'Junior'
elif idade <= 25:
    categoria = 'Senior'
else:
    categoria = 'Smaster'

if idade <= 9:
    print(f'O atleta tem {idade} anos e participa de Catergoria {categoria}')
elif idade <= 14:
    print(f'O atleta tem {idade} anod e participa da acategoria {categoria}')
elif idade <= 19:
    print(f'o atleta tem {idade} anos e prticipa da categoria {categoria}')
elif idade <= 25:
    print(f'O atleta tem {idade} anos e participa da categoria {categoria}')
else:
    print(f'O atleta tem {idade} anos e participa da categoria {categoria}')
'''
#7 Classificando Triângulos:
'''
s1 = int(input('tamanho do primeiro segmento:'))
s2 = int(input('tamanho do segundo segmento:'))
s3 = int(input('tamanho do terceiro segmento:'))

Triangulo = s3 < s1 + s2 and s2 < s1 + s3 and s1 < s3 + s2

Equilatero = s1 == s2 == s3 == s1

Isosceses = s1 == s2 and s1 != s3 or s2 == s3 and s3 != s1 or s3 == s1 and s3 != s2

Escaleno = s1 != s2 != s3 !=s1
if Triangulo and Equilatero:
    print('Esses segmentos podem formar um triângulo Equilátero')
elif Triangulo and Isosceses:
    print('Esses segmentos podem formar um triângulo Isósceles')
elif Triangulo and Escaleno:
    print('Esses segmentos podem formar um triângulo Escaleno')
else:
    print('esses segmentos nao podem formar um triângulo')

#8 Calulando IMC:
peso = float(input('digite o peso em kg:'))
altura = float(input('digite o altura em m:'))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('abaixo do peso!')
elif imc <= 25:
    print('peso ideal!')
elif imc <= 30:
    print('sobrepeso!')
elif imc <= 40:
    print('obesidade!')
else:
    print('obesidade morbida!')

print('seu imc é de {:.2f}'.format(imc))

#9 Calculando valor a ser pago:
print('{:=^40}'.format('LOJA DA ESQUINA'))
preço = float(input('Qual foi o valor gasto:'))
print('Qual vai ser o metodo de pagamento?')
print('[1] à vista')
print('[2] à vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
forma = int(input('->'))
if forma == 1:
    npreco = preço - preço * 0.1
    print(f'Voce vai pagar a vista, e o valor de {preço} vai para {npreco}')
elif forma == 2:
    npreco = preço - preço * 0.05
    print(f'Você vai pagar a vista no cartão e o valor de {preço} vai para {npreco}')
elif forma == 3:
    print(f'Voce vai pagar em 2x no cartao e preço final vai ser de {preço}')
elif forma == 4:
    parcelas = int(input('Vai parcelar em quantas vezes:'))
    npreco = preço + preço * 0.20
    v_parcelas = npreco / parcelas
    print(f'Voce vai parcelar, entao cada parcela sera {v_parcelas} e o preço final vai ser de {npreco}')
else:
    print('Inválido')
'''
#10 Jogo de Jokenpô:
import random
import time
print('-<>'*10)
print('JOKENPÔ')
print('-<>'*10)

computador = random.randint(1, 3)

jogada = int(input('''Qual sua jogada?
[1] Pedra
[2] Papel
[3] Tesoura
->'''))

if jogada < 1 or jogada > 3:
    print('jogada invalida')
    exit()

if jogada == 1:
    jogada = 'Pedra'
if jogada == 2:
    jogada = 'Papel'
if jogada == 3:
    jogada = 'Tesoura'

if computador == 1:
    computador = 'Pedra'
if computador == 2:
    computador = 'Papel'
if computador == 3:
    computador = 'Tesoura'

print('JO')
time.sleep(0.4)
print('KEN')
time.sleep(0.4)
print('PO!!!')

if (jogada == 'Pedra' and computador == 'Tesoura' or
    jogada == 'Papel' and computador == 'Pedra' or
    jogada == 'Tesoura'and computador == 'Papel'):
        print(f'Ganhou {jogada}, ganha de {computador}')
elif jogada == computador:
    print(f'Empate {jogada} é igual a {computador}')
else:
    print(f'Perdeu {computador} ganha de {jogada}')

