from inspect import signature


def clip(text:str  , /, max_len=80,*args):
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ',max_len)
            if space_before >= 0:
                end = space_after
    if end is None:
        end = len(text)
    
    return text[:end].rstrip()



def addition(**kwargs):
    return kwargs


sig = signature(addition)
# ordered mapping which maps parametrs names to corresponding aramter object
# print(sig.parameters["a"])

# bind
my_kw = {
    "name":"saeid",
    
    "addr": "Not far"
}

print(sig.bind(**my_kw))
