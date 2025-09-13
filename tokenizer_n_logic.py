
variable = {}
while_counter = 0
while_condition = []
def tokenizer(file):
    file = file.lower().split()
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
#    try:
    for i in range(len(file)):
            if file[i] == "=" and file[i+2] not in ["+", "-", "*", "/"]:
                if file[i+1].isnumeric():
                    variable[file[i-1]] = float(file[i+1])
                elif file[i+1].isalpha():
                    variable[file[i-1]] = file[i+1]
            
                elif (file[i-2] == "pile" and file[i] == "="):
                    variable[f"<:pile/>:3 {file[i-1]}"] = file[i+1]



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

            elif file[i] == "while":
                global while_counter
                while_counter += 1
                stack_open = False
                for j in range(i+1, len(file)):
                    if file[j] == ")" and stack_open == True:
                        break
                    elif stack_open == True:
                        while_condition.append(file[j])
                    elif file[j] == "(":
                        stack_open = True
                    else: # just realize i have didnt made any functions lol lets just keep it that way (°ロ°)☝ lets confuse the crap out of other ppl who will review this, i will make it so shit and so un-optimize ehehehehehe  
                        print(f"i am not gonna write every error u can do, but you made a mistake in the condition of a while loop. while_count: {while_counter} (while_count is the number of while index idk much english just understand)")
                        # i will not just nest i will build a fucking family here 
                        
    print(variable, while_condition)
                
#    except:
#        print("i am fucking lazy to write more errors just look in your .psc file bruh")
    return file

