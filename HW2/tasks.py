# 1
# float number rounded up to 2 decimals

num = float(input("Enter a number: "))
print(f"Rounded number is {num:.2f}")

# 3
# km to m and sm
km = float(input("Enter distance in kilometers: "))
meters = km * 1000
centimeters = km * 100000
print(f"{km} km is {meters} meters and {centimeters} centimeters.")

# 4
# quotent and remainder
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
division = a // b
remainder = a % b
print(f"Division: {division}")
print(f"Remainder: {remainder}")

# 5
# celcius to fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} C is equal to {fahrenheit} F")

# 6
# last digits
num = int(input("Enter a number: "))
last_digit = num % 10
print(f"The last digit is: {last_digit}")

# 7
# even or not
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# STRING QUESTIONS
# 1
# calculate age
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
current_year = 2025
age = current_year - birth_year
print(f"{name}, you are {age} years old.")

# 2
# car name
txt = "LMaasleitbtui"
word1 = txt[::2]
word2 = txt[1::2]
print(f"Word 1: {word1}")
print(f"Word 2: {word2}")


# 3
# string manipulation
str = input("Enter a string: ")
print(len(str))
print(str.upper())
print(str.lower())

# 4
# is palindrome
string = input("Enter a string: ")
if string == string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is NOT a palindrome.")

# 5
# how many vowels
string = input("Enter a string: ").lower()
vowel_count = 0
consonant_count = 0
for char in string:
    if char.isalpha():
        if char in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")

# 6
# if string is in another string
string1 = input("bigger string ")
string2 = input("smaller string ")
if string2 in string1:
    print(f'"{string2}" is found in "{string1}".')
else:
    print(f'"{string2}" is NOT found in "{string1}".')

# 7
# replace
sentence = input("Enter a sentence: ")
word_to_replace = input("Enter the word to replace: ")
replacement_word = input("Enter the new word: ")
new_sentence = sentence.replace(word_to_replace, replacement_word)
print("Updated sentence:", new_sentence)

# 8
# string first and last chars
string = input("Enter a string: ")
if len(string) > 0:
    print(f"First character: {string[0]}")
    print(f"Last character: {string[-1]}")
else:
    print("You entered an empty string.")

# 9
# reverse string
string = input("Enter a string: ")
reversed_string = string[::-1]
print("Reversed string:", reversed_string)

# 10
# word count
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words:", word_count)

# 11
# digits exist
string = input("Enter a string: ")
contains_digit = False
for char in string:
    if char.isdigit():
        contains_digit = True
        break
if contains_digit:
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")

# 12
# seperator
words = input("Enter words separated by spaces: ").split()
separator = '-'
joined_string = separator.join(words)
print("Joined string:", joined_string)

# 13
# remove spaces
string = input("Enter a string: ")
no_spaces = string.replace(" ", "")
print("String without spaces:", no_spaces)

# 14
# if strings equal
string1 = input("first string: ")
string2 = input("second string: ")
if string1 == string2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")

# 15
# acronym maker
sentence = input("Enter a sentence: ")
acronym = ""
for word in sentence.split():
    acronym += word[0].upper()
print("Acronym:", acronym)

# 16
# remove chars
string = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")
new_string = string.replace(char_to_remove, "")
print("String after removal:", new_string)

# 17
# replace vowels
string = input("Enter a string: ")
vowels = "AEIOUaeiou"
new_string = ""
for char in string:
    if char in vowels:
        new_string += "*"
    else:
        new_string += char
print("Modified string:", new_string)

# 18
# print start end words
string = input("Enter a string: ")
start_word = input("Enter the starting word: ")
end_word = input("Enter the ending word: ")

if string.startswith(start_word) and string.endswith(end_word):
    print(True)
else:
    print(False)


# BOOLEAN DATA TYPE QUESTIONS
# 1
# is password and username empty
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()
if username and password:
    print("Login successful.")
else:
    print("Username and password is empty.")

# 2
# equal or not
a = int(input())
b = int(input())
print(a == b)

# 3
# if positive and even
num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("True")
else:
    print("False")

# 4
# check not the same
a = int(input())
b = int(input())
c = int(input())
print(a != b and b != c and a != c)

# 5
# check if the string same length
str1 = input()
str2 = input()
print(len(str1) == len(str2))

# 6
# if number divisible by 3 and 5
num = int(input())
print(num % 3 == 0 and num % 5 == 0)

# 7
# check if sum is bigger than 50.8
a = float(input())
b = float(input())
print((a + b) > 50.8)

# check if num is 10<num<20 inclusive
num = int(input())
print(10 <= num <= 20)
