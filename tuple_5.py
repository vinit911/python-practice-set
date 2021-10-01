'''
Create a list of tuples from given list having number and its cube in each tuple
'''
t1 = (1,2,3,4,5,6,7)
# l1 = list(t1)
l1 = [(x,x*x*x) for x   in t1]

l2 = [(x,pow(x,3)) for x in t1]
print(l1)
print(l2)