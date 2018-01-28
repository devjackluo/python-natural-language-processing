from sidestuff.base import Base

##################################
##################################
# assert hasattr(Base, 'foo'), "you monkey!"
# class Derived(Base):
#
#     def bar(self):
#         return self.foo()


##################################
##################################
class Derived(Base):

    def bar(self):
        return 'bar'

# p1 = Derived()
# print(p1.foo())




