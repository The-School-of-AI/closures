######################################################################################################
def closure1():
    ''' closure that takes a function and then check whether the function passed has a docstring
with more than 50 characters. 50 is stored as a free variable '''
    num_chars = 50

    def check_inner(fn):
        text = fn.__doc__
        if len(text) > num_chars:
            print(f"Doc string of function {fn.__name__} has more than {num_chars} characters")
            return len(text)
        else:
            print(f"Doc string of function {fn.__name__} has less than {num_chars} characters")
            return len(text)

    return check_inner

def add_fn(a, b):
    """ This function """
    return a + b
def mul_fn(a, b):
    """ This function takes two number and returns multiplication of those numbers"""
    return a * b
def div_fn(a, b):
    """ This function """
    if b > 0:
        return a/b
    else:
        raise ValueError("denominator cannot be ZERO")

##############################################################################################################
def closure2():
    ''' Closure that gives the next Fibonacci number
    Output: As the function is called it prints the next fibonacci number
    fib1 and fib2 are the free variables that gets modified in the inner function "next_fib()" '''
    fib1 = 0
    fib2 = 1
    def next_fib():
        nonlocal fib1,fib2
        nth = fib1 + fib2
        fib1 = fib2
        fib2 = nth
        print(fib2)
        return fib2

    return next_fib
#tt = closure2()
#tt.__code__.co_freevars
##############################################################################################################
###################################################################################################################
'''We wrote a closure that counts how many times a function was called.
 Write a new one that can keep a track of how many times add/mul/div functions were called, 
 and update a global dictionary variable with the counts (+ 6 tests) - 250'''

count_fn_dict = dict()
def closure3(fn):
    global count_fn_dict
    if not callable(fn):
        raise ValueError('function should be the passed as an argument')
    def count_fn(*args,**kwargs):
        name = fn.__name__
        result = fn(*args,**kwargs)
        print(f'result of the function {name} is {result}')
        if name in count_fn_dict:
            count_fn_dict[name] += 1
        else:
            count_fn_dict[name] = 1
        return count_fn_dict
    return count_fn
#counter_add = closure3(add_fn)
#counter_mul = closure3(mul_fn)
#counter_div = closure3(div_fn)
#counter_add.__code__.co_freevars

#counter_add(12,10)
#counter_mul(23,45)
#counter_add(210,412)
#counter_div(12,44)
##############################################################################################################
'''Modify above such that now we can pass in different dictionary variables to update 
different dictionaries (+ 6 tests) - 250'''
add_fn_dict = dict()
mul_fn_dict = dict()
div_fn_dict = dict()
def closure4(fn):
    """Takes function (add/mult/div functions) as input and returns the output from the inner function 'counting'
    which is a dictionary that keeps track of number of times a function is called and a separate dictionary for
    each function."""
    count = 0
    count_dict = dict()
    if not callable(fn):
        raise ValueError('function should be the passed as an argument')

    def counting(*args, **kwargs):
        nonlocal count, count_dict
        result = fn(*args, **kwargs)
        count += 1
        count_dict[fn.__name__] = count
        return count_dict

    return counting


#counter_add_fn = closure4(add_fn)
#counter_mul_fn = closure4(mul_fn)
#counter_div_fn = closure4(div_fn)

#add_dict_count = counter_add_fn(3, 4)
#add_dict_count = counter_add_fn(4, 5)
#mul_dict_count = counter_mul_fn(4, 5)
#div_dict_count = counter_div_fn(8, 0)
#mul_dict_count = counter_mul_fn(4, 7)
#div_dict_count = counter_div_fn(8, 0)
#mul_dict_count = counter_mul_fn(4, 3)
#print(f'Results on how many times add_fn function is called: {add_dict_count}')
#print(f'Results on how many times mul_fn function is called: {mul_dict_count}')
#print(f'Results on how many times div_fn function is called: {div_dict_count}')
