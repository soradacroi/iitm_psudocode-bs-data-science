import helper as h


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
    #print(file)
    if not file:
        raise ValueError("File is empty.")

    i = 0
    while i < len(file):
        if file[i] == "while":
            # Parse while condition
            cond = []
            todo = []
            if file[i+1] == "(":
                j = i+2
                while file[j] != ")":
                    cond.append(file[j])
                    j += 1
                j += 1  # skip ')'
                # Parse while body
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
                # Call while_helper for this loop
                h.while_helper(variable, cond, todo)
                i = j  # move to after this while block
        else:
            h.logic(i, file)
        i += 1

    return file

