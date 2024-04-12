# whenever you are overriding a method in a subclass it is essential to call the corresponding
# method in the base class.
# this is done by using super built-in function.

class Animal:
    def __setitem__(self, name):
        self.name = name
    
    def __getitem__(self, item):
        return repr(self) 


class Bird(Animal):
    def __setitem__(self, name):
        return super(Bird, self).__setitem__(name)

# multiple inheritance and method resoltion order introduction
class Root:

    def ping(self):
        print(f"{self}.ping() in Root")

    def pong(self):
        print(f"{self}.pong() in Root")

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        return f"<instance of {cls_name}>"


class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()


class B(Root):
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')


class Leaf(A,B):
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()

leaf1 = Leaf()
# leaf1.ping()
# leaf1.pong()

print(Leaf.mro()) # [<class '__main__.Leaf'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Root'>, <class 'object'>]


# tkinter multiple inheritance hierarchy
import tkinter
def show_mro(cls):
    mros = [cls.__name__ for cls in cls.mro()]
    rp_mro = " ".join(mros)
    print(rp_mro)

show_mro(tkinter.Text)