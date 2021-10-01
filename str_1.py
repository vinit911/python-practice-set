'''
Python program to check whether the string is Symmetrical or Palindrome
'''
def symmetrical(palindrome):
        l = (len(palindrome))
        print("Length of the string = ",l)
        l = int(l/2)
        a = slice(0 , l)
        b = slice(l,l*2)
        print("First half :- \t",palindrome[a])
        print("Second half:- \t",palindrome[b])
        p1 = palindrome[a]
        p2 = palindrome[b]
        if p1 == p2:
            print("It is symentric")
        else:
            print("Not an symentric")

def check_palindrome(palindrome):
    #    print( palindrome(reversed))
    rev = palindrome[::-1]
    print("The reverse of string :- ",rev)
    print("Its palindrome") if(palindrome == rev) else print("Its not palindrome")


    # for i in palindrome:
    #     if i ==
    

palindrome = input("Enter your string :- ")
print("*"*50)
symmetrical(palindrome)
print("*"*50)
check_palindrome(palindrome)
print("*"*50)
