#ex 05 sucessor e antecessor
#n1 = int(input('Digite um numero!'))
#s = n1+1
#a = n1-1
#print('Analisando o número digitado, seu sucessor é {}, e seu antecessor é {}'.format(s,a))

#ex 06 dobro triplo e Raiz
#n1 = int(input('Digite um numero!'))
#d = n1*2
#t = n1*3
#r = n1**2
#print('O dobro de {} é {}, o Triplo é {} e ainda a Raiz quadrada é {}'.format(n1, d, t, r))


#ex 07 média
#nome = input('Qual o numero da matricula ou nome do aluno?')
#n1 = float(input('Qual a primeira nota do aluno?'))
#n2 = float(input('Qual a segunda nota do aluno?'))
#m = (n1+n2) /2
#print('A média do aluno é {:.2f}!!'.format(m))

#ex 09 tabuada

"""""
n = int(input('Digite um número para saber a sua tabuada!'))
print (n*'*')
print ('{} x {:2} = {}'.format(n, 1, n*1))
print ('{} x {:2} = {}'.format(n, 2, n*2))
print ('{} x {:2} = {}'.format(n, 3, n*3))
print ('{} x {:2} = {}'.format(n, 4, n*4))
print ('{} x {:2} = {}'.format(n, 5, n*5))
print ('{} x {:2} = {}'.format(n, 6, n*6))
print ('{} x {:2} = {}'.format(n, 7, n*7))
print ('{} x {:2} = {}'.format(n, 8, n*8))
print ('{} x {:2} = {}'.format(n, 9, n*9))
print ('{} x {:2} = {}'.format(n, 10, n*10))
print (n*'*')
"""""

"""""
#ex10 conversor

r = float(input('Qual valor você quer comprar em dolares?'))
d = 4.73
e = 5.23
print ('O valor de R${} Reais, dá para comprar {:.2f} Dolares e {:.2f} Euros!'.format(r, r/d, r/e))
"""""

#ex 11 area e pintura de parede
"""""
larg = float(input('Qual a largura total da parede?'))
alt = float(input('Qual a altura total da parede?'))
parede = larg*alt
tinta = parede/2
print ('Você precisará de {} litros de tinta para pintar {}M² de parede!'.format(tinta, parede))
"""""

#ex 12 desconto %

#v1 = float(input('Qual valor do produto?'))
#vd = v1 - (v1 * 5 / 100)
#ou vf = v1 - vd
#print ('Olha só!, esse produto está com desconto de 5% e portanto custará {:.2f}'.format(vd))

"""""
#ex 13 aumento %
cargo = input('Qual seu cargo?')
salario = float(input('Qual seu salario bruto atual? R$'))
novosalario = salario + (salario * 15 / 100)
print ('Seu cargo teve um aumento de 15% e atualmente é R${}!'.format(novosalario))
"""""


#ex 14 conversor temperatura

t1 = float(input('Qual a temperatura em ºC ?'))
tf = (t1 * 1.8) + 32
print ('Convertendo a temperatura {} ºC para Fahrenheit é {}ºF!'.format(t1, tf))


