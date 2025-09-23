import helper as wh


variable = {}

def tokenizer(file):
    file = file.split()
    temp = []
    for i in file:
        if i.endswith(")"):
            temp.append(i[:-1])
            temp.append(")")
        elif i.startswith("("):
            temp.append("(")
            temp.append(i[1:])
        elif i.endswith("}"):
            temp.append(i[:-1])
            temp.append("}")
        elif i.startswith("{"):
            temp.append("{")
            temp.append(i[1:])
        else:
            temp.append(i)
    temp = [s for s in temp if s.strip() != ""]
    file = temp
    print(file)
    if not file:
        raise ValueError("File is empty.")

    i = 0
    while i < len(file):
        if file[i] == "while":
            
            cond = []
            todo = []
            if file[i+1] == "(":
                j = i+2
                while file[j] != ")":
                    cond.append(file[j])
                    j += 1
                j += 1  
                
                if file[j] == "{":
                    j += 1
                    brace_count = 1
                    while brace_count > 0:
                        if file[j] == "{":
                            brace_count += 1
                        elif file[j] == "}":
                            brace_count -= 1
                            if brace_count == 0:
                                break
                        if brace_count > 0:
                            todo.append(file[j])
                        j += 1
                
                wh.while_helper(variable, cond, todo)
                i = j 
        else:
            logic(i, file)
        i += 1

    return file

def logic(i, file):
        if file[i] == "=" and file[i+2] not in ["+", "-", "*", "/"]:
                    if file[i+1].isnumeric():
                        variable[file[i-1]] = float(file[i+1])
                    elif file[i+1].isalpha():
                        variable[file[i-1]] = file[i+1]
                
                    elif (file[i-2] == "pile" and file[i] == "="):
                        variable[("pile", file[i-1])] = file[i+1]


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
