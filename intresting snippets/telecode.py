# started writing this snippet right after
# I realized how match/case expressions are used in python


# function takes your phone number as an argument and specifies the location using match/case
def country_tel(tel):
    if isinstance(tel , str):
        sub = [f"+{tel[0]}", tel[1:]]
    else:
        tel_to_str = str(tel)
        sub = [f"+{tel_to_str[0]}", tel_to_str[1:]]
    
    match sub:
        case ['+1', number]:
            print("calling from the US")
        case ['+5', number]:
            return "calling from Africa"
        case ['+3' | "+4", number]:
            return "calling from Europe" 
        case _:
            return "calling from the unknown continent"