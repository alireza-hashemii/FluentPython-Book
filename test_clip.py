from clip import clip
from inspect import signature

# print(clip.__defaults__)
# print(clip.__code__)
# print(clip.__code__.co_varnames)
# print(clip.__code__.co_argcount)

sig = signature(clip)
print(sig)
for name,param in sig.parameters.items():
    print(param.kind, ': ',name, '= ',param.default)