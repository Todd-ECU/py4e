# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 01:01:18 2020

3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

@author: toddv
"""

hrs = input("Enter Hours: ")
rate = input("Enter Rate Per Hour: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("***Error, please enter numeric input***")
    raise SystemExit()

otr = r*1.5
oth = h - 40    
regpay = h * r
otpay = oth * otr
bh = h - oth
basepay = bh * r

if h <= 40:
    print(regpay)
else:    
    print(basepay + otpay)

    
    

