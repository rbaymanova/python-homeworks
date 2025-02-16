d = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'nested': {'x': 10}}
d2 = {'e': 4, 'f': 5}
keys_list = ['g', 'h']
values_list = [7, 8]
tuple_kv = (('i', 9), ('j', 10))

#1
if 'b' in d:
    value_b = d['b']
else:
    value_b = 'Not Found'
print(value_b)

if 'z' in d:
    value_z = d['z']
else:
    value_z = 'Not Found'
print(value_z)

#2
if 'c' in d:
    print(True)
else:
    print(False)

#3
count_keys = 0
for key in d:
    count_keys += 1
print(count_keys)

#4
all_keys = []
for key in d:
    all_keys.append(key)
print(all_keys)

#5
all_values = []
for key in d:
    all_values.append(d[key])
print(all_values)

#6
merged = d.copy()
for key in d2:
    merged[key] = d2[key]
print(merged)

#7
d_copy = d.copy()
if 'a' in d_copy:
    del d_copy['a']
print(d_copy)

#8
d_clear = d.copy()
d_clear.clear()
print(d_clear)

#9
if len(d) == 0:
    print(True)
else:
    print(False)

#10
if 'b' in d:
    pair = ('b', d['b'])
else:
    pair = None
print(pair)

#11
d_update = d.copy()
d_update['a'] = 100
print(d_update)

#12
value_to_count = 2
occurrence = 0
for key in d:
    if d[key] == value_to_count:
        occurrence += 1
print(occurrence)

#13
inverted = {}
for key in d:
    value = d[key]
    if type(value) != dict:
        inverted[value] = key
print(inverted)

#14
value_to_find = 2
keys_with_value = []
for key in d:
    if d[key] == value_to_find:
        keys_with_value.append(key)
print(keys_with_value)

#15
dict_from_lists = {}
for i in range(len(keys_list)):
    dict_from_lists[keys_list[i]] = values_list[i]
print(dict_from_lists)

#16
has_nested = False
for key in d:
    if type(d[key]) == dict:
        has_nested = True
        break
print(has_nested)

#17
if 'nested' in d:
    nested_value = d['nested'].get('x', None)
else:
    nested_value = None
print(nested_value)

#18
default_value = d.get('z', 'default')
print(default_value)

#19
unique_values = []
for key in d:
    if d[key] not in unique_values:
        unique_values.append(d[key])
print(len(unique_values))

#20
sorted_by_key = {}
sorted_keys = list(d.keys())
sorted_keys.sort()
for key in sorted_keys:
    sorted_by_key[key] = d[key]
print(sorted_by_key)

#21
items = list(d.items())
items.sort(key=lambda item: item[1])
sorted_by_value = {}
for key, value in items:
    sorted_by_value[key] = value
print(sorted_by_value)

#22
filtered = {}
for key in d:
    if type(d[key]) == int and d[key] > 2:
        filtered[key] = d[key]
print(filtered)

#23
common_keys_found = False
for key in d:
    if key in d2:
        common_keys_found = True
        break
print(common_keys_found)

#24
dict_from_tuple = {}
for pair in tuple_kv:
    key, value = pair
    dict_from_tuple[key] = value
print(dict_from_tuple)

#25
first_pair = None
for key in d:
    first_pair = (key, d[key])
    break
print(first_pair)
