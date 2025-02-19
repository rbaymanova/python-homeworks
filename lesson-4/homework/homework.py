from random import randint
from collections import Counter

# 1
# Return uncommon elements of lists. Order of elements does not matter.
list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))
set1, set2 = set(list1), set(list2)
result = list(set1.symmetric_difference(set2))
print("Uncommon elements:", result)

# 2
# Print the square of each number which is less than n on a separate line.
a = int(input())
for i in range(1, a):
    print(i*i)

# 3
# put underscore every third letter with some conditions
txt = input("Enter a string:")
skip = "aeiou"
result = ""
cnt =0
for i in range(len(txt)):
    cnt+=1
    result+=txt[i]
    if i!=len(txt)-1 and cnt>=3 and txt[i] not in skip:
        skip +=txt[i]
        result+="_"
        cnt=0
print(result)

# 4
# guessing game with randint
while True:
    n = 0
    rand_guess = randint(1, 100)
    while n < 10:
        user_guess = int(input("Guess a number between 1 and 100: "))
        if user_guess > rand_guess:
            print("Too high")
            n += 1
        elif user_guess < rand_guess:
            print("Too low")
            n += 1
        elif user_guess < 0 or user_guess > 100:
            print("Invalid input")
        else:
            print("Correct")
            break
        if n>10:
            print("Too many guesses")
            break
    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() not in ["y", "yes", "ok"]:
        break

# 5
# checks password security(?)
password = input("Enter your password: ")
if len(password) > 8:
    c = False
    for char in password:
        if char.isupper():
            c = True
            break
    if c:
        print("Password is strong")
    else:
        print("Password must contain at least one uppercase letter.")
else:
    print("Your password is too short.")

# 6
# prime numbers from 1 to 100
arr = []
for i in range(2, 100):
    for j in range(2, i//2 + 1):
        if i % j == 0:
            break
    else:
        arr.append(i)
print(arr)


