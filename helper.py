import json

piles = {}

def load_pile(pile_name, filename):
    with open(filename, 'r') as f:
        piles[pile_name] = json.load(f)


variable = {}
while_condition, while_todo = [], []
dataset = {}

def is_pile_tuple(x):
    if x[0] == "pile" and x[1].isnumeric():
        return True
    else:
        return False


def while_helper(var, while_con, while_stuff):
    global variable, while_condition, while_todo
    variable = var
    while_condition, while_todo = while_con, while_stuff
    #print(while_stuff)
    for i in variable:
        #print(i)
        if is_pile_tuple(i):
            with open(rf'{variable[i]}', 'r') as f:
                dataset[i[1]] = json.load(f)
    con_tf = True
    #print(while_todo, while_con)
    while con_tf:
        con_tf = while_looper_con(while_con)
        while_looper_todo(while_todo)


    print(dataset)
#print(is_pile_tuple("ss"))
#print(is_pile_tuple(("pile","1")))


def if_condition():
    ...


def while_looper_todo(while_todo):
    for i, elem in enumerate(while_todo):
        logic(i, while_todo)
        



def while_looper_con(while_con):
    if ">=" in while_con:
        if while_con[0] in variable:
            if variable[while_con[0]] >= float(while_con[2]):
                return True
            else:
                return False

    elif ">" in while_con:
        if while_con[0] in variable:
            if variable[while_con[0]] > float(while_con[2]):
                return True
            else:
                return False
    elif "<=" in while_con:
        if while_con[0] in variable:
            if variable[while_con[0]] <= float(while_con[2]):
                return True
            else:
                return False

    elif "<" in while_con:
        if while_con[0] in variable:
            if variable[while_con[0]] < float(while_con[2]):
                return True
            else:
                return False
    elif "==" in while_con:
        if while_con[0] in variable:
            if variable[while_con[0]] == float(while_con[2]):
                return True
            else:
                return False

    elif "!=" in while_con:
        if while_con[0] in variable:
            if variable[while_con[0]] != float(while_con[2]):
                return True
            else:
                return False
            
    

def logic(i, file):
        if file[i] == "=" and file[i+2] not in ["+", "-", "*", "/"]:
                    if file[i+1].isnumeric():
                        variable[file[i-1]] = float(file[i+1])
                    elif file[i+1].isalpha():
                        variable[file[i-1]] = file[i+1]
                
                    elif (file[i-2] == "pile" and file[i] == "="):
                        variable[("pile", file[i-1])] = file[i+1]

        elif file[i] == "print" and file[i + 2] in variable:
            print(variable[file[i + 2]])


        elif file[i] == "=" and file[i+2] in ["+", "-", "*", "/"]:
                if (file[i+1] in variable.keys() and file[i+3].isnumeric()):
                    if file[i+2] == "+":
                        variable[file[i-1]] = variable[file[i+1]] + float(file[i+3])
                    elif file[i+2] == "-":
                        variable[file[i-1]] = variable[file[i+1]] - float(file[i+3])
                    elif file[i+2] == "*":
                        variable[file[i-1]] = variable[file[i+1]] * float(file[i+3])
                    elif file[i+2] == "/":
                        variable[file[i-1]] = variable[file[i+1]] / float(file[i+3])
                elif (file[i+1].isnumeric() and file[i+3] in variable.keys()):
                    if file[i+2] == "+":
                        variable[file[i-1]] = float(file[i+1]) + variable[file[i+3]]
                    elif file[i+2] == "-":
                        variable[file[i-1]] = float(file[i+1]) - variable[file[i+3]]
                    elif file[i+2] == "*":
                        variable[file[i-1]] = float(file[i+1]) * variable[file[i+3]]
                    elif file[i+2] == "/":
                        variable[file[i-1]] = float(file[i+1]) / variable[file[i+3]]
                elif (file[i+1] in variable.keys() and file[i+3] in variable.keys()):
                    if file[i+2] == "+":
                        variable[file[i-1]] = variable[file[i+1]] + variable[file[i+3]]
                    elif file[i+2] == "-":
                        variable[file[i-1]] = variable[file[i+1]] - variable[file[i+3]]
                    elif file[i+2] == "*":
                        variable[file[i-1]] = variable[file[i+1]] * variable[file[i+3]]
                    elif file[i+2] == "/":
                        variable[file[i-1]] = variable[file[i+1]] / variable[file[i+3]]
                elif (file[i+1].isnumeric() and file[i+3].isnumeric()):
                    if file[i+2] == "+":
                        variable[file[i-1]] = float(file[i+1]) + float(file[i+3])
                    elif file[i+2] == "-":
                        variable[file[i-1]] = float(file[i+1]) - float(file[i+3])
                    elif file[i+2] == "*":
                        variable[file[i-1]] = float(file[i+1]) * float(file[i+3])
                    elif file[i+2] == "/":
                        variable[file[i-1]] = float(file[i+1]) / float(file[i+3])
                elif (file[i+1].isalpha() and file[i+3].isalpha()):
                    if file[i+2] == "+":
                        variable[file[i-1]] = file[i+1] + " " + file[i+3]
