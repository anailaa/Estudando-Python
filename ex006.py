
# Leia um numero e mostre seu dobro, triplo e raiz quadrada #

n1 = int(input('Digite um numero: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
print('O dobro de {} é {},\n o triplo é {} \n e a raiz quadrada é {:.2f}'.format(n1,d,t,r))
# \n é quebra de linha
#:.2f é a quantidade de casa depois da virgula.
