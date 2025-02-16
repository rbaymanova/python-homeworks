tup = (1, 2, 3, 2, 4, 1, 5)
tup2 = (6, 7, 8)
lst = [10, 20, 30]

#1
print(tup.count(2))

#2
print(max(tup))

#3
print(min(tup))

#4
print(2 in tup)

#5
print(tup[0] if tup else None)

#6
print(tup[-1] if tup else None)

#7
print(len(tup))

#8
print(tup[:3])

#9
print(tup + tup2)

#10
print(tup == ())

#11
print([i for i, x in enumerate(tup) if x == 2])

#12
unique_tup = tuple(sorted(set(tup)))
second_largest = unique_tup[-2] if len(unique_tup) >= 2 else None
print(second_largest)

#13
second_smallest = unique_tup[1] if len(unique_tup) >= 2 else None
print(second_smallest)

#14
single_elem_tup = (99,)
print(single_elem_tup)

#15
converted_tup = tuple(lst)
print(converted_tup)

#16
print(tup == tuple(sorted(tup)))

#17
subtup = tup[1:5]
print(max(subtup))

#18
print(min(subtup))

#19
t_list = list(tup)
if 2 in t_list:
    t_list.remove(2)
new_tup = tuple(t_list)
print(new_tup)

#20


#21
tup = (1, 2, 3)
repeat = 3
result1 = []
for x in tup:
    for i in range(repeat):
        result1.append(x)
repeated_tup = tuple(result1)
print(repeated_tup)

#22
range_tup = tuple(range(1, 11))
print(range_tup)

#23
print(tup[::-1])

#24
print(tup == tup[::-1])

#25
unique_in_order = []
for x in tup:
    if x not in unique_in_order:
        unique_in_order.append(x)
print(tuple(unique_in_order))
