###nome= input('Qual é o seu nome ?')
##print('Prazer te conhecer{:>20} !'.format(nome))

n1= int(input('Um Valor:'))
n2= int(input('Outro Valor:'))
s= n1 + n2
m= n1 * n2
d= n1 / n2
di= n1 // n2
e= n1 ** n2

print('A Soma vale {}, \nProduto é {} e a Divisão é {:.3f}'.format(s, m, d),end= '')
print('Divisão inteira {}, e potência {}'.format(di, e))
