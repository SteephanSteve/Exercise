#!usr/bin/python

a=raw_input("Enter the year :")
if type(a)==int:
 if a%4==0:
    print(a,"is a leap year")
 else:
    print(a,"is not a leap year")
else:
    print "Invaid input"
