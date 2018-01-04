import random



class Table_file:
    fname = "tables\\sudoku_tables.txt"
    tables = []


    def __init__(self, fname = "tables\\sudoku_tables.txt"):
        self.fname = fname
        table = [[]]
        with open(self.fname) as f:
            lines = f.readlines()
        lines = list(map(lambda s: s.strip(), lines))
        #print(lines)

        #print(len(lines))

        line_count = len(lines)
        table_count = line_count / 10


        tables = [[[]]]
        k = 0
        while(k < table_count):
            table = []
            for i in range(9):
                row = []
                for j in range(9):
                    row.append(lines[k * 10 + i + 1][j])
                    """
                    if(not k*10 + i+1 > line_count):
                        row.append(lines[k*10 + i+1][j])
                    else:
                        print("List index out of range: " + str(k*10 + i+1) + " > " + str(line_count))
                    """
                    #print(str(k) + " - " + str(i) + " - " + str(j))
                #print(row)
                table.append(row)
            #print(table)
            tables.append(table)
            k += 1
        self.tables = tables
        #print(tables)



    def get_table(self, seed=-1):
        # Return random table
        if(seed == -1 or not self.is_number(seed)):
            if(not self.is_number(seed)):
                print("Seed is not a number!")
            rnd = random.randint(0, len(self.tables))
            return self.get_table(rnd)
        # Return table by seed
        else:
            return self.tables[int(seed) % len(self.tables)]




    def get_random_table(self):
        rnd = random.randint(0, len(self.tables))
        return self.get_table(rnd)


    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False