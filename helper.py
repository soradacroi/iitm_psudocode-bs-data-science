variables = {}
while_condition, while_todo = [], []
def while_helper(var, while_con, while_stuff):
    global variables, while_condition, while_todo
    variables = var
    while_condition, while_todo = while_con, while_stuff
    print(variables, while_condition, while_todo)



def if_condition():
    ...
