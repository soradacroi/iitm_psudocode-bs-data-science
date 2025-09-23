import json
import tokenizer_n_logic as tnl

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
    #print(while_stuff)
    for i in variables:
        #print(i)
        if is_pile_tuple(i):
            with open(rf'{variables[i]}', 'r') as f:
                dataset[i[1]] = json.load(f)
    con_tf = True
    print(while_todo, while_con)
    while con_tf:
        con_tf = while_looper_con(while_con)
        while_looper_todo(while_todo)


                #print(dataset)
#print(is_pile_tuple("ss"))
#print(is_pile_tuple(("pile","1")))


def if_condition():
    ...


def while_looper_todo(while_todo):
    for i, elem in enumerate(while_todo):
        if elem == "print" and while_todo[i + 2] in variables:
            print(variables[while_todo[i + 2]])

        tnl.logic(i, while_todo)
        



def while_looper_con(while_con):
    if ">=" in while_con:
        if while_con[0] in variables:
            if variables[while_con[0]] >= float(while_con[2]):
                return True
            else:
                return False

    elif ">" in while_con:
        if while_con[0] in variables:
            if variables[while_con[0]] > float(while_con[2]):
                return True
            else:
                return False
    elif "<=" in while_con:
        if while_con[0] in variables:
            if variables[while_con[0]] <= float(while_con[2]):
                return True
            else:
                return False

    elif "<" in while_con:
        if while_con[0] in variables:
            if variables[while_con[0]] < float(while_con[2]):
                return True
            else:
                return False
    if "==" in while_con:
        if while_con[0] in variables:
            if variables[while_con[0]] == float(while_con[2]):
                return True
            else:
                return False

    elif "!=" in while_con:
        if while_con[0] in variables:
            if variables[while_con[0]] != float(while_con[2]):
                return True
            else:
                return False


