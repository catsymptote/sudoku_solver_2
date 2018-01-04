import sys

def printer(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            sys.stdout.write(str(table[i][j]) + "\t")
        sys.stdout.write("\n\n")
    sys.stdout.flush()