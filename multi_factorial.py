# Multiple factorial of n

number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for n in number_list:
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(str(n) + "! = " + str(fact))