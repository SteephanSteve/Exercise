#!usr/bin/python

a="hello"

if (len(a)==1 and a in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
  if a in "aeiouAEIOU" :
   print "Vowel"
  else:
   print "Consonant"
else:
  print "Invalid Input"


    
