def factorial(n): 
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)

using_map = list(map(factorial, range(5)))
using_liscoms = [factorial(n) for n in range(5)] # output: [1, 1, 2, 6, 24]
using_concomps =  [factorial(n) for n in range(6) if n % 2]


from functools import reduce
from operator import add
# two ways of doing same work.
summation_answer = reduce(add , range(100))
second_way = sum(range(100))


# other reducing functions
# weird behaviour!!
dummy_conatainer = [False, 7]
print(any(dummy_conatainer)) # returns true if at least 1 element is truthy
print(all(dummy_conatainer)) # returns true if all the elements are truthy





