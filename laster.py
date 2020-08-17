fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
hand = open(fname)

di = dict()
for lin in hand:
    if not lin.startswith("From "):
        continue
    else:    
        
        lin = lin.split()
        lin = lin[5]
        lin = lin[0:2]
       
        di[lin]=di.get(lin,0) + 1

li = list()

for value,count in di.items():
        li.append((value,count))

li.sort()
for value,count in li:
    print (value,count) 