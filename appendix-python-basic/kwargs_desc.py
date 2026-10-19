# 说明自动接收的参数


def f1(name, *, age, **kwargs):
    print(f"{name=} \n{age=} \n{kwargs=}")


"""
name='Alice' 
age=30 
kwargs={'city': 'New York', 'country': 'USA'}
"""
f1("Alice", age=30, city="New York", country="USA")


def f2(name, *, age=None, **kwargs):
    print(f"{name=} \n{age=} \n{kwargs=}")

"""
name='Alice' 
age=None 
kwargs={'city': 'New York', 'country': 'USA'}
"""
f2("Alice", city="New York", country="USA")
