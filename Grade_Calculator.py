# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 00:38:53 2020
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
@author: toddv -- 

"ok you can work now....."
"""

score = input("Enter Score: ")
try:
    final = float(score)
except:
    print("***Error, please enter numeric input***") 
    raise SystemExit()
    
if (final > 1.0 or final < 0.0):
    print("***Error, score must be between 0.0 and 1.0")
    raise SystemExit() 
                  
elif final >= 0.9:
    print("A")
elif final < 0.9 and final >= 0.8:
    print("B")
elif final < 0.8 and final >= 0.7:
    print("C")
elif final < 0.7 and final >= 0.6:
    print("D")
else:
    print("F")

       
    
       
    