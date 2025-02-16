#1
#count the occurrence
lst = [1, 2, 3, 4, 2, 2, 5]
lst2 = [6, 7, 8]
mixed_lst = [1, -2, 3, -4, 5]

element = 6;
occurrences = lst.count(element)
print(f"occurrences: {occurrences}")

#2
total1 = sum(lst)
print(f"total: {total1}")

#3
max1 = max(lst)
print(f"max: {max1}" )

#4
min1 = min(lst)
print(f"min: {min1}")

#5
print(element in lst)

#6,7
if lst != []:
    print(lst[0])
    print(lst[-1])

#8
new_lst = lst[:3]
print(new_lst)

#9
newNewLst = lst[::-1]
print(newNewLst)

#10
nnn_lst = sorted(lst)
print(nnn_lst)

#11
unique_lst = []
for x in lst:
    if x not in unique_lst:
        unique_lst.append(x)
print(unique_lst)

#12
lst_insert = lst.copy()
lst_insert.insert(2, 99)
print(lst_insert)

#13
print(lst.index(2))

#14
print(lst == [])

#15
print(sum(1 for x in lst if x % 2 == 0))

#16
print(sum(1 for x in lst if x % 2 != 0))

#17
concat_lst = lst + lst2
print(concat_lst)

#18


#19
lst_replace = lst.copy()
if 2 in lst_replace:
    lst_replace[lst_replace.index(2)] = 99
print(lst_replace)

#20,21
unique_nums = list(set(lst))
unique_nums.sort()
if len(unique_nums) >= 2:
    second_largest = unique_nums[-2]
    second_smallest = unique_nums[1]
else:
    second_largest = None
    second_smallest = None
print(second_largest)
print(second_smallest)


#22
even_lst = [x for x in lst if x % 2 == 0]
print(even_lst)

#23
odd_lst = [x for x in lst if x % 2 != 0]
print(odd_lst)

#24
print(len(lst))

#25
copy_lst = lst.copy()
print(copy_lst)

#26
n = len(lst)
middle = lst[n//2] if n % 2 == 1 else lst[n//2 - 1:n//2 + 1]
print(middle)

#27
subsection = lst[1:5]
max_value = max(subsection)
print(max_value)

#28
print(min(subsection))

#29
lst_removed = lst.copy()
if 0 <= 2 < len(lst_removed):
    lst_removed.pop(2)
print(lst_removed)

#30
print(lst == sorted(lst))

#31
repeat_number = 3
repeated_lst = [x for x in lst for _ in range(repeat_number)]
print(repeated_lst)

#32
merged_sorted = sorted(lst + lst2)
print(merged_sorted)

#33
all_indices = [i for i, x in enumerate(lst) if x == 2]
print(all_indices)

#34
rotated_lst = [lst[-1]] + lst[:-1] if lst else []
print(rotated_lst)

#35
range_lst = list(range(1, 11))
print(range_lst)

#36
print(sum(x for x in lst if x > 0))

#37
print(sum(x for x in mixed_lst if x < 0))

#38
print(lst == lst[::-1])

#39
n_sub = 2
nested_lst = [lst[i:i+n_sub] for i in range(0, len(lst), n_sub)]
print(nested_lst)

#40
unique_in_order = []
for x in lst:
    if x not in unique_in_order:
        unique_in_order.append(x)
print(unique_in_order)