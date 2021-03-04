import time, sys
indent = 0
indent_increasing = True

try:
    while True:
        print(' ' * indent, end = '')#{end = ''} =
        print('********')
        time.sleep(0.1) #pause for 1/10 of a second

        if indent_increasing: #increase the number of spaces
            indent += 1
            if indent == 10: #when indent increas to 5 ,trun indent_increasing into False
                indent_increasing = False

        else:           #decrease the number of spaces
            indent -= 1
            if indent == 0: #when indent decreas to 0 ,trun indent_increasing into False
                indent_increasing = True

except KeyboardInterrupt:  #let KeyboardInterrupt error dispear
    sys.exit

