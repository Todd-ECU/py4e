def sum_elements(l):
    s = l[0]
    for element in l[1:]:
        s += element
    return s
sum_elements([1, 2, 3])
