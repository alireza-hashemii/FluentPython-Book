# closure litrally is a function which extends the scope of itself.
# you just use it while working with a function located in another function.
# by using closure you're gonna have access to local variables of outter function
# so if you need permission to work with vars which are neither global nor local
# it it's own space. closure is here for you.

# here I write a function that keeps tracking of inputs and calculator the mean of that.
# functional solution
# outer function
def make_averager():
    series = []
    # inner function
    def averager(__new_value):
        series.append(__new_value)
        total = sum(series)
        return total / len(series)
    return averager
# This function returns a callable.

# Test
d = make_averager()
print(d(10))
print(d(12))

# version2 - using a broken strategy. However ; where is broken?
def make_averager():
    total = 0
    count = 0
    # inner function
    def averager(__new_value):
        total += __new_value
        count += 1
        return total / count
    return averager

# Test
dl = make_averager()
print(dl(10))

# UnboundLocalError: local variable 'total' referenced before assignment
# you'd probably observe the same error as I do. that's because total += value
# is creating a new object and augmented assigment operation doesn't work for muteables
# so here a new value is created and immediately += operator is called.
# which brings us the error. so what's the solution??
# the solution is to use nonlocal keyword.

def make_averager():

    total = 0
    count = 0
    # inner function
    def averager(__new_value):
        nonlocal total , count
        total += __new_value
        count += 1
        return total / count
    return averager

# Test
dl2 = make_averager()
print(dl2(10))
print(12)