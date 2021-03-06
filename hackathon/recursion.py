def sum_array(array):

    '''Return sum of all items in array'''
    if (len(array))<=1:
        return array[0]
    else:
        return array.pop(0)+sum_array(array)

fibonacci_cache = {0:0,1:1,2:1}
def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    value = fibonacci(n-2) + fibonacci(n-1)
    fibonacci_cache[n] = value
    return value
factorial_cache = {}
def factorial(n):

    '''Return n!'''

    if n in factorial_cache:
        return factorial_cache[n]

    if n <2:
        value = 1
    else:
        value = n*factorial(n-1)
    factorial_cache[n]=value
    return value

def reverse(word):

    '''Return word in reverse'''

    if len(word)<=1:
        return word
    else:
        return word[-1]+reverse(word[:-1])
