#!usr/bin/python

a="One"
if (type(a)==str and len(a)==1):
 if a in "aeiou" :
  print "Vowel"
 else:
  print "Consonant"
else:
 print "Invalid Input"
