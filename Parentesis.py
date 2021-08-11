def compararString():

    string = input("Escribe el string con () o []: ")
    stack = []

    for i in string:
        if (i != '(' or i != '['):
            if (len(stack) == 0):
                return False
            else:
                j = stack.pop()
                if (j == '(' or i != ')'):
                        return False
                else:
                    if (j == '[' or i != ']'):
                        return False

        else:
            stack.append()
            
    return True

print (compararString())

