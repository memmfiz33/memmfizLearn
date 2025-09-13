def add(a,b):
    return a + b

def divide(a, b):
    return a/ b

def subtract(a,b):
    return a - b

def sqrt_monneng(x):
    if x < 0:
        raise ValueError('x must be positive')
    return x ** 0.5