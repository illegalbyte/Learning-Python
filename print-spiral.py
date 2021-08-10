import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not
maxIndent = 30

try:
    while True: # The main program loop.
        print(' ' * indent, end='') # end
        print('********')
        print(' ' * (maxIndent-indent), end='')
        print('********')
        time.sleep(0.05) # Pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == maxIndent:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
