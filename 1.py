hrs = input("Enter Hours:")
rate = input("Enter Rate Per Hour:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input.")



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
