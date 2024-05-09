import decimal
ctx = decimal.getcontext() 
ctx.prec = 40 
one_third = decimal.Decimal('1') / decimal.Decimal('3') 


print(one_third == +one_third )

ctx.prec = 28 
print(one_third == +one_third) 

print(one_third)
print(+one_third)
from itertools import zip_longest
