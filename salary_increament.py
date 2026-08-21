# Increase the salary of the amazing worker only
# the amazing worker are of idx 1, 3, 5

salary_list = [11, 22, 33, 44, 55, 66, 77, 88]
amazing_worker = [1, 3, 5]

emp = len(salary_list)     # This will show total employee 

for i in range(0, emp):
    if i in amazing_worker:
        salary_list[i] += 10
    else:
        salary_list[i] += 5
        
print(salary_list)