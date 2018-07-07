#!usr/bin/python

a=int(input("Enter the number :"))
rev=0
while a>0:
 l=a%10
 rev=rev*10+l
 a=a//10
print rev
 
