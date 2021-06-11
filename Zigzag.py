import time, sys
ident = 0
identIncreasing = True

try:
    while True: # Main Loop
        print(' ' * ident, end= '')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.

        if identIncreasing:
            ident = ident + 1 # Increase number of spaces
            if ident == 15:
                identIncreasing = False # Change direction
        else:
            ident = ident - 1 # Decrease number of spaces
            if ident == 0:
                identIncreasing = True # Change direction
except KeyboardInterrupt:
    sys.exit()