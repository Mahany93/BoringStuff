import time, sys
indent = 0  # How many spaces to indent
indentIncreasing= True     # Whether the indentation is increasing or not.

try:
    while True:     # Main loop
        print(' ' * indent,end='')
        print('********')
        time.sleep(0.1) # pause for 1/10 of a second.

        if indentIncreasing:    # Increase number of spaces
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False    #Change direction
        
        else:   # Decrease number of spaces
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()


        