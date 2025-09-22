import helper as wh

variable = {}
while_counter = 0
while_condition = []
damn = []
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
    #print(file)
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

            elif file[i] == "while":
                temp_while_condition = []
                tempdo = []
                stack_open = False
                global while_counter
                while_counter += 1
                damn_counter = 0
                for j in range(i+1, len(file)):
                    
                    if file[j] == ")" and stack_open == True:
                        temp_while_condition = []
                        stack_open = False
                        
                    elif stack_open == True:
                        temp_while_condition.append(file[j])
                        while_condition = temp_while_condition
                    elif file[j] == "(" and file[j-1] == "while" :
                        stack_open = True


                    if file[j] == "}":
                        damn_counter -= 1
                    elif file[j] == "{":
                        damn_counter += 1
                    elif damn_counter != 0:
                        tempdo.append(file[j])
                        damn = tempdo
                    elif damn_counter == 0:    
                        tempdo = []


                        
                    #else: # just realize i have didnt made any functions lol lets just keep it that way (°ロ°)☝ lets confuse the crap out of other ppl who will review this, i will make it so shit and so un-optimize ehehehehehe  
                    #    print(f"i am not gonna write every error u can do, but you made a mistake in the condition of a while loop. while_count: {while_counter} (while_count is the number of while index idk much english just understand)")
                
                wh.while_helper(variable, while_condition, damn)

                    

    

#    except:
#        print("i am fucking lazy to write more errors just look in your .psc file bruh")
    return file

