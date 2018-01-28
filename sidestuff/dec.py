from time import time

def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print(after-before)
        return rv
    return f

def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                rv = f(*args, **kwargs)
                print('running {.__name__}'.format(f))
                #print(rv)
            return rv
        return wrapper
    return inner


#@timer
@ntimes(2)
def add(x, y=10):
    return x + y
# decorator is almost same as  add = timer(add)

@timer
def sub(x, y=10):
    return x + y


print(add(10))
print(add(20,30))
print(add('a', 'b'))

print(sub(10))
print(sub(20,30))
print(sub('a', 'b'))


