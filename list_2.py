'''
Python program to swap two elements in a list

'''
def swap(a,b):
    return b,a 

swap_list = [1,2,3,4,5,6]
s1 = int(input("Enter the First element"))
s2 = int(input("Enter the second element"))
# print(swap_list.index(s1))
a = 10 
b = 20
print(swap(a,b))
# print(a,b)
if s1 and s2 in swap_list:
    # print("in if ")
    l1 = swap_list.index(s1)
    l2 = swap_list.index(s2)
    swap(l1,l2)


# swap_list.index(s2) = s1

print(swap_list)