for i in [5,4,3,2,1] :
    print(i)
print('Blastoff!')  




count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)


found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15, 3] : 
   if value == 3 :
       found = True
   else: 
       found = False
   print(found, value)
print('After', found)

