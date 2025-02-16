set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
list1 = [1, 2, 3, 3, 4, 5, 5, 6]
list2 = [5, 6, 7, 8, 9]

#1
union_set = set1 | set2
print(union_set)

#2
intersection_set = set1 & set2
print(intersection_set)

#3
difference_set = set1 - set2
print(difference_set)

#4
print(set1 <= union_set)

#5
print(3 in set1)

#6
print(len(set1))

#7
converted_set = set(list1)
print(converted_set)

#8
set3 = set1.copy()
set3.discard(2)
print(set3)

#9
set4 = set1.copy()
set4.clear()
print(set4)

#10
print(len(set1) == 0)

#11
sym_diff = set1 ^ set2
print(sym_diff)

#12
set5 = set1.copy()
set5.add(7)
print(set5)

#13
set6 = set1.copy()
popped = set6.pop()  
print(popped, set6)

#14
print(max(set1))

#15
print(min(set1))

#16
even_set = {x for x in set1 if x % 2 == 0}
print(even_set)

#17
odd_set = {x for x in set1 if x % 2 != 0}
print(odd_set)

#18
range_set = set(range(1, 11))
print(range_set)

#19
merged_set = set(list1 + list2)
print(merged_set)

#20
print(set1.isdisjoint({7, 8, 9}))

#21
list_with_duplicates = [1, 2, 3, 3, 4, 4, 5]
unique_list = list(set(list_with_duplicates))
print(unique_list)

#22
unique_count = len(set(list_with_duplicates))
print(unique_count)

#23
import random
random_set = {random.randint(1, 100) for _ in range(5)}
print(random_set)
