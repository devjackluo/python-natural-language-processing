import time


def add(x,y):
    return x + y

class Adder:
    def __call__(self, x,y):
        return x + y

print(add(2,2))
add2 = Adder()
print(add2(2,2))

# def compute():
#     rv = []
#     for i in range(10):
#         time.sleep(0.5)
#         rv.append(i)
#     return rv
# #compute()

def compute():
    for i in range(64):
        time.sleep(.5)
        yield i

prev = 0
total = 1
for i in compute():
    newtotal = total + prev
    prev = total
    total = newtotal
    print(total)


# class Compute:
#     def __iter__(self):
#         self.last = 0
#         return self
#     def __next__(self):
#         rv = self.last
#         self.last += 1
#         if self.last > 10:
#             raise StopIteration()
#         time.sleep(.5)
#         return rv
#
# for val in Compute():
#     print(val)


# class Api:
#     def run_this_first(self):
#         first()
#     def run_this_second(self):
#         second()
#     def run_this_last(self):
#         last()








