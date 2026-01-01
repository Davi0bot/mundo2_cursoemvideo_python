#DEIXO DESDE AQUI CLARO, SÃO EXEMPLOS BASICOS DE EXERCICIOS COM IF E ELSE
#aula, basico de if e else

nome = input('Digite seu nome:')
if nome == 'gustavo':
    pass
print('uau')
print('Bom dia' ,nome)

# desafios

#n1, jogo basico de adivinhaçao com if e else
import random
num = random.randint(0,5)
tentativa = int(input('tente adivinhar o numero! '))
if tentativa == num:
    print('você acertou!')
else:
    print('você errou')

print('o numero era {}'.format(num))

#n2, aplica multa se a velocidade é muito alta
vel = int(input('digite sua velocidade:'))
if vel > 80:
    print('O lilite de velocidade é 80km/h')
    print(f'sua multa é R${(vel - 80)*7} vai com calma')
else:
    print('tenha um bom dia!')

#n3, verifica se é par ou impar
num = int(input('digite um numero:'))
if num % 2 == 0:
    print('par')
else:
    print('impar')
    
#n4, calcula custo da viagem dependendo da distancia
viagem = int(input('digite a distanncia da viagem:'))
if viagem <= 200:
    print('a viagem vai custar R${:.2f}'.format(viagem * 0.50))
else:
    print('a viagem vai custar {:.2f}'.format(viagem * 0.45))


#n5, ve se um ano é bissexto
import datetime
ano_atual = datetime.date.today().year
ano = int(input('digite o ano ou 0 para ano atual:'))
if ano % 4 == 0 and ano != 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é bissexto'.format(ano))
elif ano == 0:
    if ano_atual %4 == 0:
        print('{} é bisssexto'.format(ano_atual))
    else:
        print('{} não é bissexto'.format(ano_atual))
else:
    print('{} nao é bissexto'.format(ano))

#n6, pega 3 numeros e ve qual é maior e qul é menor

n1 = int(input('digite o primeiro numero:'))
n2 = int(input('digite o segundo numero:'))
n3 = int(input('digite o terceiro numero:'))

if n1 > n2 and n1 > n3:
    print('{} é o maior'.format(n1))
if n2 > n1 and n2 > n3:
    print('{} é o maior'.format(n2))
if n3 > n1 and n3 > n2:
    print('{} é o maior'.format(n3))

if n1 < n2 and n1 < n3:
    print('{} é o menor'.format(n1))
if n2 < n1 and n2 < n3:
    print('{} é o menor'.format(n2))
if n3 < n1 and n3 < n2:
    print('{} é o menor'.format(n3))


#n7, da aumento de salario dependo quanto ganha

sal = float(input('digite o salario:'))
if sal <= 1250:
    sal = sal * 0.15 + sal
else:
    sal = sal * 0.10 + sal
print('seu novo salario é R${:.2f}'.format(sal))

#n8, ve se é possivel formar um triangulo com tais retas

s1 = int(input('tamanho do primeiro segmento:'))
s2 = int(input('tamanho do segundo segmento:'))
s3 = int(input('tamanho do terceiro segmento'))

if s3 < s1 + s2 and s2 < s1 + s3 and s1 < s3 + s2:
    print('Esses segmentos podem formar um triângulo')
else:
    print('esses segmentos nao podem formar um triângulo')

'''
#fim dos exercicios/desafios
'''
#exemplo de exercicio com if
while True:
    
    try:
        idade = int(input('digite sua idade:'))
        if idade <0:
            print('essa nao é uma idade valida')
            continue
        elif idade <= 12:
            print('criança')
        elif idade < 18:
            print('adolescente')
        elif idade < 60:
            print('adulto')
        else:
            print('idoso')
        break
    except ValueError:
        print('digite apenas numeros')

