#!usr/bin/python

def fact(n):
    if n == 0:
        return 1
    elif n<=20 and n>=0:
        return n * fact(n-1)
    else:
        return "Invalid input"
         
a=int(raw_input("Enter the NO. :")) 
print fact(a)
