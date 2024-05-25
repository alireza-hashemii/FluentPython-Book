import sys


class ReverseMatch:
    def __enter__(self):
        self.o = sys.stdout.write
        sys.stdout.write = self.text_out
        return "Sample"

    def text_out(self, text):
        self.o(text[::-1])


    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.o
        if any([exc_type, exc_value, traceback]) is True:
            print("Shit")
        if exc_type is ZeroDivisionError:
            print("Hell")
            return True
           

# with ReverseMatch() as rvm:
#     print(rvm)
#     print(type(rvm))
#     print("Isn't all this amazing?")
#     print(5 / 0)


class StrippedVersion:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.striped
        return None
    
    def striped(self, text):
        self.original_write(text.strip())

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print("Haven't you crossed the boundaries?")
        return True
    
# with StrippedVersion() as result:
#     print("A     ")
#     print("H")
# print("o")

from contextlib import contextmanager

@contextmanager
def looking_glass():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])
    
    sys.stdout.write = reverse_write
    try:
        yield "Job" 
    except ZeroDivisionError:
        print("Not now")
    finally:
        sys.stdout.write = original_write 


with looking_glass() as rvm:
    print(rvm)
    print(type(rvm))
    print("Isn't all this amazing?")
    print(5 / 0)

print("Ok DADA")