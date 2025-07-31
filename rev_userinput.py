# This program reverses the userinput.

a = input("Type Anything Here: ")
a_list = list(a)
a_list.reverse()
a = ''.join(a_list)
print(a)