#                                           #
# Estudando tratamento de strings no python #
#                                           #

a = input('Digite algo: ')
print('O tipo primitivo desse valor é?', type(a))
print('Só tem espaço?', a.isspace())
print('É um numero?', a.isnumeric())
print('É alfabetica?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Está em maiusculo?', a.isupper())
print('Está em minusculo', a.islower())
print('Está capitalizada?', a.istitle())