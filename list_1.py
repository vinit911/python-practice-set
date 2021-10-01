'''
Python program to interchange first and last elements in a list
'''

l1 = [1,2,3,4,5,6]
print("List before modification:\t",l1)
l1[0],l1[-1] = l1[-1],l1[0]

print("List after modification: \t",l1)