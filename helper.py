
import json

variables = {}
while_condition, while_todo = [], []
dataset = {}

def is_pile_tuple(x):
    if x[0] == "pile" and x[1].isnumeric():
        return True
    else:
        return False



def while_helper(var, while_con, while_stuff):
    global variables, while_condition, while_todo
    variables = var
    while_condition, while_todo = while_con, while_stuff

    print(while_stuff)
    for i in variables:
        #print(i)
        if is_pile_tuple(i):
            with open(rf'{variables[i]}', 'r') as f:
                dataset[i[1]] = json.load(f)

    while_looper(while_con, while_stuff)


                #print(dataset)
#print(is_pile_tuple("ss"))
#print(is_pile_tuple(("pile","1")))



def if_condition():
    ...

def while_looper(while_con, while_stuff):
    if ">=" in while_con:
        if while_con[0] in variables:
            print("ok")

