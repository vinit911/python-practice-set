'''
Python program to print even length words in a string
'''
sentence = "This is my name vinit and I am a good boy"
l1 = sentence.split()
l2 =[]
print(sentence.split())
for x in l1:
    if len(x)%2 == 0:
        l2.append(x)

print("List of the words having Even number",l2)
