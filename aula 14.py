#Aula 14 curso em video Python
#Loops de While
#Alguns dos exercicios sao melhroes com o loop for

for i in range(1,10):#for quando sabe onde termina while quando nao sabe
    print(i)
print('Fim')

c = int(input('Digite um numero: '))
while c < 100:
    print(c)
    c += 1
print('Fim')

#Exercicios:

#n1 Vendo sexo e so aceitando M ou F
while True:
    sexo = str(input('Digite seu sexo: ')).upper()
    if sexo == 'M' or sexo == 'F':
        print('Ok')
        break
    else:
        print('Digite um sexo valido(M/F): ')
        continue

#n2 adivinhaçao de numero 0-10
from random import randint
tent = 0
comp = randint(0, 10)
while True:
    play = int(input('Chute o numero que o computador escolheu: '))
    tent += 1
    if play == comp:
        print(f'Voce acertou com {tent} tentativas')
        break
    else:
        print('Errou tente novamente!')
        continue

#n3 semi calculadora

while True:
    resultado = 0
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o sengundo número: '))

    açao = int(input('Para somar digite[1]\n'
                     'Para subtrair digite[2]\n'
                     'Para multiplicar digite[3]\n'
                     'Para dividir digite[4]\n'
                     'Para ver maior/menor digite[5]\n'
                     'Para digitar outros numeros digite[6]\n'
                     '->'))
    if açao == 1:
       resultado = num1 + num2
       print(f'{num1} + {num2} = {resultado}')
    elif açao == 2:
        resultado = num1 - num2
        print(f'{num1} - {num2} = {resultado}')
    elif açao == 3:
        resultado = num1 * num2
        print(f'{num1} x {num2} = {resultado}')
    elif açao == 4:
        resultado = num1/num2
        print(f'{num1} ÷ {num2} = {resultado}')
    elif açao == 5:
        print(f'O maior é {max(num1,num2)} e o menor é {min(num1,num2)}')
    elif açao == 6:
        continue
    else:
        print('Digite um valor correto([1] [2] [3] [4] [5] [6])')
        continue

    break


#n4 fatorial usando while
fac = int(input('Qual numero deseja saber o fatorial: '))
n_n = 0
res = fac -1
ces = 0
while n_n < fac:
    ces = res * fac
    res -= 1
    fac = ces
    n_n += 1
    print(ces)





#n5 progressao aritimetica com while
n = 0
razao = int(input('Qual a razão entre os numero quer? '))#com for é muito melhor
while True:
    print(n)
    n += razao
    if n >= 999:
        break



#n6 progressao aritimetica com quantos termos o usuario quiser
termo = int(input('Quantos termos desaja saber da PA? '))
raz = int(input('E qual a razão entre eles? '))
n1 = 0
n2 = 0
while n1 < termo:
    n1 += 1
    n2 += raz #com for é muito melhor
    print(n2)


#n7 sequencia de fibonacci
n = 0
ent = int(input('Quantos numeros da sequencia de Fibonacci voce quer ver: '))
f1 = 0
f2 = 1
f3 = 0
while n < ent:
    n += 1
    f3 = f2 + f1
    print(f3)
    f1 = f2
    f2 = f3

#n8 ler numeros e so parar quando o usuario digitar 999 e depois mostrar a soma entre os numeros digitados desconsiderando o 999(flag)
x = 0
nuns = []
qnt_x = 0
while x != 999:
    x = int(input('Digite numeros:'))
    if x != 999:
        nuns.append(x)
        qnt_x += 1
print(f'Desconsiderando o \033[32m999\033[m você digitou {qnt_x} números e a soma entre eles é',sum(nuns))

#n9 ler numeros pedindo ao usuario se quer parar e ver a media entre os numeros o maior e o menor
lst = []
med = 0
while True:
    inp = int(input('Quantos número quer digitar: '))
    for i in range(1,inp+1):
        nn = int(input(f'Digite o {i}º número: '))
        lst.append(nn)
        med += 1
    desc = int(input('\nPara ver a média digite [1];\n'
    'Para ver o maior e o menor digite [2];\n'
    'Para recomeçar digite 3;\n'
    'Para encerrar digite 0;\n->'))
    if desc == 1:
        print(sum(lst)/med)
    elif desc == 2:
        print(f'O menor é {min(lst)} e o maior é {max(lst)}')
    elif desc == 3:
        continue
    elif desc == 0:
        break
    else:
        print('\033[31mInválido!\033[m')
        continue

