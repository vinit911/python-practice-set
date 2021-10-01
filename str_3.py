'''
Ways to remove i’th character from string in Python
'''
str1 = input("Enter your string :- ") 
ith = int(input("Enter the ith element :- "))
l1 = list(str1) # Convert input string into list

if(ith > len(str1)):
    print("please enter valid position ")

else :
    l1.pop(ith-1) # This line will delete (pop) the ith element from the list 

    str2 = "" # Empty string
    for x in l1:
        str2 += x # This convert list into string again 


    print("The string without ith element <---",str2,"--->")
