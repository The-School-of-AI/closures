import pytest
import Assignment_7
import os
import re
import inspect

############################################################################################################

def test_readme_exists():
    assert os.path.isfile('README.md'), 'README.md file missing'

def test_closure1_check_nchar_freevar():
    ''' Checks for number of free variables '''
    t = Assignment_7.closure1()
    assert len(t.__code__.co_freevars) == 1, f"number of free variables for this closure should be 1 which is number of characters"

def test_indentations_closure1():
    ''' Returns pass if used 4 spaces for each level of syntactically significant indenting'''
    lines = inspect.getsource(Assignment_7.closure1)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Script contains misplaced indentations"
        assert len(re.sub(r'[^ ]','',space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_output_closure1():
    def add(a, b):
        """ This function """
        return a + b

    def mul(a, b):
        """ This function takes two number and returns multiplication of those numbers"""
        return a * b

    def div(a, b):
        """ This function """
        if b > 0:
            return a / b
        else:
            print("denominator cannot be ZERO")

    t = Assignment_7.closure1()
    assert t(add) < 50,'Number of characters in Doc string of function add is less than 50 characters'
    assert t(mul) > 50,'Number of characters in Doc string of function mul is greater than 50 characters'
    assert t(div) < 50, 'Number of characters in Doc string of function div is less than 50 characters'

def test_clsoure1():
    '''Checking if its a closure and returns a function '''
    t = Assignment_7.closure1()
    assert inspect.isfunction(t) == True, 'You are not returning a function in closure'

def test_closure2_check_nchar_freevar():
    ''' Checks for number of free variables '''
    t = Assignment_7.closure2()
    assert len(t.__code__.co_freevars) == 2, f"number of free variables for this closure are 2 which is fib1=0,fib2=1"

def test_closure2_nextfib():
    ''' Checks for number of free variables '''
    t = Assignment_7.closure2()
    for i in range(3):
        t()
    assert t() == 5, f"4th number in the fibonacci series is 5"
    for i in range(3):
        t()
    assert t() == 34, f"8th number in the fibonacci series is 34"

def test_closure3_fn_freevar():
    def add_fn(a, b):
        return a + b

    t = Assignment_7.closure3(add_fn)
    assert len(t.__code__.co_freevars) == 1, f"number of free variables for this closure is 1: 'fn' "

def test_closure3_isfn():
    def add_fn(a, b):
        return a + b

    t = Assignment_7.closure3(add_fn)
    assert inspect.isfunction(t) == True, 'You are not returning a function in closure'

def test_closure3_function_call_valueerror():
    with pytest.raises(ValueError):
        Assignment_7.closure3(1000)

def test_closure3_dict():
    def add_fn(a, b):
        return a + b
    def mul_fn(a, b):
        return a * b

    def div_fn(a, b):
        """ This function """
        if b > 0:
            return a / b
        else:
            print("denominator cannot be ZERO")

    #t = Assignment_7.closure3(add_fn)
    counter_add = Assignment_7.closure3(add_fn)
    counter_mul = Assignment_7.closure3(mul_fn)
    counter_div = Assignment_7.closure3(div_fn)

    counter_dict = counter_add(12, 10)
    counter_dict = counter_div(12, 44)
    counter_dict = counter_mul(23, 45)
    counter_dict = counter_div(12, 44)
    counter_dict = counter_add(210, 412)
    counter_dict = counter_div(12, 44)

    print(f'Dictionary counting number of times a function is called : {counter_dict}')
    assert counter_dict['add_fn'] == 2, f"number of times add function is called is 2 "
    assert counter_dict['mul_fn'] == 1, f"number of times mul function is called is 1 "
    assert counter_dict['div_fn'] == 3, f"number of times div function is called is 3 "

def test_closure4_dict():
    def add_fn(a, b):
        return a + b

    def mul_fn(a, b):
        return a * b

    def div_fn(a, b):
        return a / b if b > 0 else 'Division by zero error'

    counter_add = Assignment_7.closure4(add_fn)
    counter_mul = Assignment_7.closure4(mul_fn)
    counter_div = Assignment_7.closure4(div_fn)

    div_dict = counter_div(8, 0)
    div_dict = counter_div(18, 3)
    mul_dict = counter_mul(623, 54)
    add_dict = counter_add(34, 87)
    div_dict = counter_div(6,3)
    assert div_dict['div_fn'] == 3, f'div_fn is called 3 times '
    assert mul_dict['mul_fn'] == 1, f'mul_fn is called 1 time '
    assert add_dict['add_fn'] == 1, f'add_fn is called 1 time '

def test_closure4_function_call_valueerror():
    with pytest.raises(ValueError):
        Assignment_7.closure4(1000)

def test_closure4_isfn():
    def add_fn(a, b):
        return a + b

    t = Assignment_7.closure4(add_fn)
    assert inspect.isfunction(t) == True, 'You are not returning a function in closure'

def test_closure4_fn_freevar():
    def add_fn(a, b):
        return a + b

    t = Assignment_7.closure4(add_fn)
    assert len(t.__code__.co_freevars) == 3, f"number of free variables for this closure is 3: 'count', 'count_dict', 'fn' "