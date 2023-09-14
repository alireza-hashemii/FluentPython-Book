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