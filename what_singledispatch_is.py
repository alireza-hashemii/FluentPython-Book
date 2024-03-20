# a group of funcions that do the same task but the process of
# doing it may vary among them. So every single one of them 
# would do it in a separate way or method.

# this exapmle shows a base function called the htmlizer. This functions receives 
# python objects of different types and convert them into html tags separately.

from functools import singledispatch
from collections import abc
import fractions
import decimal
import html
import numbers


@singledispatch
def htmlizer(object: any) -> str:
    content = html.escape(repr(object))
    return f"<pre>{content}</pre>"


@htmlizer.register
def _(text: str) -> str: 
    content = html.escape(text).replace('\n', '<br/>\n')
    return f'<p>{content}</p>'


@htmlizer.register
def _(seq: abc.Sequence) -> str:
    inner = "<li>\n</li>".join(htmlizer(item) for item in seq)
    return "<ul>\n<li>" + inner + "</li>\n</ul>"



@htmlizer.register 
def _(n: numbers.Integral) -> str:
    return f'<pre>{n} (0x{n:x})</pre>'


@htmlizer.register 
def _(n: bool) -> str:
    return f'<pre>{n}</pre>'

# you can put type hint for parametr and it works right 
# or you can specify the type of input parameter in the 
# paranthesis of Base.register()
@htmlizer.register(fractions.Fraction) 
def _(x) -> str:
    frac = fractions.Fraction(x)
    return f'<pre>{frac.numerator}/{frac.denominator}</pre>'



@htmlizer.register(float)
def _(x) -> str:
    frac = fractions.Fraction(x).limit_denominator()
    return f'<pre>{x} ({frac.numerator}/{frac.denominator})</pre>'