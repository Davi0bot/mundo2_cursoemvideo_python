#loops FOR
#Explicaçao da aula
i=int(input('Inicio:'))
f=int(input('Fim:'))
p=int(input('Passo:'))
for i in range(i,f,p):
    print(i)
for i in range(10):
    print('<>-',end='')

#Desafios/exercicios:

#n1: contagem regressiva
i = 0
from time import sleep
contagem = 10
for i in range(11):
    print(contagem)
    sleep(1)
    contagem-=1



#n2: pares de 1-50
for i in range(0,50,2):
    print(i,end=' ')

#n3: soma de impares e multiplos de 3 entre 1-500
i = 0
impares = 0
quantia = 0
for i in range(0,500,3):
    if i % 2 != 0:
        print(i, end =' ')
        impares += i
        quantia += 1
print(f'\nA soma dos, {quantia} é {impares}')


#n4: Tabuada melhorada
numero = int(input('qual tabuada deseja saber? '))
for j in range(11):
    print(f'{numero} x {j} = {numero*j}')

#n5: vendo se é par ou impar
n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
n3 = int(input('digite mais um numero: '))
n4 = int(input('digite um numero: '))
n5 = int(input('digite outro numero: '))
n6 = int(input('digite o ultimo numero: '))
numeros = [n1, n2, n3, n4, n5, n6]
for n in numeros:
    if n %2 ==0:
        n = n+n
        print(n)
n+=n
print(n)



#n6: vendo PA(progressao aritimetica) 10 primeiros termos
i = 0
termo = int(input('Digite o termo: '))
razão = int(input('Digite a razão entre eles:'))
for i in range(termo,termo + (razão*10),razão):
    print(i,end=' ')

#n7: Vendo se numero é primo
cont = 0
np = int(input('Digite um numero:'))
ndivi = []
for i in range(1, np+1):
    if np % i == 0:
        cont += 1
        ndivi.append(i)
if q == 2:
    print(f'{np} só é divisivel por 1 e {np} então ele é primo')
else:
    print(f'{np} foi divisivel por {ndivi} entao nao é primo')


#n8: vendo se frase é palidromo desconsiderando espaços
i = 0
frase1 = input('Digite uma frase: ')
frase = ''.join(frase1.split())
invertida = frase[::-1]
print(f'{frase1} ao contrario é {invertida}')
if invertida == frase:
    print('Por isso é um palindromo')
else:
    print('Por isso não é um palindromo')

#n9: ler data de nascimento e ver se é maior de idade

from datetime import datetime
i = 0
anos = []
n = 0
m_i = 0
ano_atual = datetime.now().year
for i in range(7):
    n += 1
    nascimento = int(input(f'Digite o {n}ª data de nascimento:'))
    anos.append(nascimento)

for nascimento in anos:
    if ano_atual - nascimento >= 18:
        m_i += 1
print(f'temos {m_i} pessoas maiores de idade e {1 + i - m_i} menores')



#n10: vendo maior e menor peso

i = 0
pesos = []
for i in range(5):
    peso = float(input('Digite seu peso: '))
    pesos.append(peso)
print(f'O mais pesado pesa {max(pesos)}kg.\nO mais leve pesa {min(pesos)}kg.')

#11 media de idades homem mais velho mulherer com menos de 20 anos

i = 0
nomes = []
generos = []
n = 0
idades = 0
cont_id = []
menor_20 = 0
for i in range(1,5):
    n += 1
    nome = str(input(f'Digite o {n}º nome: '))
    idade = int(input(f'Digite a {n}ª idade: '))
    sexo = str(input(f'Digite o seu genero (M/F): ')).upper()
    if sexo == 'M':
        cont_id.append(idade)
    if sexo == 'F' and idade < 20:
        menor_20 += 1
    nomes.append(nome)
    idades += idade
    generos.append(sexo)
print(f'Dentre os nomes citados: {nomes}\n')
print(f'O homem mais velho tem {max(cont_id)} anos\n')
print(f'A média de idades é {idades/4}\n')
print(f'Os generos são {generos}\n')
print(f'E {menor_20} mulheres são menores de 20 anos')