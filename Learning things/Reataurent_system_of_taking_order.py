# This will indicate which waiter is assigned to each table

class waiter:
    def __init__(self):
        self.table = []
        
    def add_table(self, table_number):
        self.table.append(table_number)
        
aditya = waiter()
rohan = waiter()

aditya.add_table(5)
aditya.add_table(4)

rohan.add_table(3)
rohan.add_table(2)

print(aditya.table)
print(rohan.table)