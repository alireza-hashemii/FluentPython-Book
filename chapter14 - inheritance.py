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