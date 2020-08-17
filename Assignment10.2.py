fname = input("Enter file name: ")
if len(fname) < 1 : fname = "my.txt"
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1

print(di)  

x = sorted(di.keys())
print(x)