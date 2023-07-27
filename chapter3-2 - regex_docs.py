import re
# putting re module under investigation
txt = """salam man alireza hashemsis 
    hastam o emrooz mikham rajebvs 
    y mozoo kheyli jazab ba shoma 
    sohbat konam berim k shoroos 
    """
txt2 = 'salams-'
print(re.search("^s s-$",txt2))

text2 = 4
