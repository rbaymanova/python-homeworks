#1
#float number rounded up to 2 decimals

# num = float(input("Enter a number: "))
# print(f"Rounded number is {num:.2f}")

#3
#km to m and sm
# km = float(input("Enter distance in kilometers: "))
# meters = km * 1000
# centimeters = km * 100000
# print(f"{km} km is {meters} meters and {centimeters} centimeters.")

#4
#quotent and remainder
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
#
# division = a // b
# remainder = a % b
#
# print(f"Division: {division}")
# print(f"Remainder: {remainder}")

#5
#celcius to fahrenheit
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius} C is equal to {fahrenheit} F")

#6
#last digits
# num = int(input("Enter a number: "))
# last_digit = num % 10
# print(f"The last digit is: {last_digit}")

#7
#even or not
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

#STRING QUESTIONS
#1
#calculate age
# name = input("Enter your name: ")
# birth_year = int(input("Enter your year of birth: "))
# current_year = 2025
# age = current_year - birth_year
# print(f"{name}, you are {age} years old.")

#2
#car name
# txt = "LMaasleitbtui"
# car_name = txt[1] + txt[3:6] + txt[8] + txt[10:12]
# print(f"Car name: {car_name}")

#3
#string manipulation
# str = input("Enter a string: ")
# print(len(str))
# print(str.upper())
# print(str.lower())

#4
#is palindrome
# string = input("Enter a string: ")
# if string == string[::-1]:
#     print(f"{string} is a palindrome.")
# else:
#     print(f"{string} is NOT a palindrome.")

#5
#how many vowels
# string = input("Enter a string: ").lower()
# vowel_count = 0
# consonant_count = 0
# for char in string:
#     if char.isalpha():
#         if char in "aeiou":
#             vowel_count += 1
#         else:
#             consonant_count += 1
#
# print(f"Vowels: {vowel_count}")
# print(f"Consonants: {consonant_count}")

#6
#if string is in another string
# string1 = input("bigger string ")
# string2 = input("smaller string ")
# if string2 in string1:
#     print(f'"{string2}" is found in "{string1}".')
# else:
#     print(f'"{string2}" is NOT found in "{string1}".')

#7
#replace
# sentence = input("Enter a sentence: ")
# word_to_replace = input("Enter the word to replace: ")
# replacement_word = input("Enter the new word: ")
# new_sentence = sentence.replace(word_to_replace, replacement_word)
# print("Updated sentence:", new_sentence)

#8
#string first and last chars
# string = input("Enter a string: ")
# if len(string) > 0:
#     print(f"First character: {string[0]}")
#     print(f"Last character: {string[-1]}")
# else:
#     print("You entered an empty string.")

#9
#reverse string
# string = input("Enter a string: ")
# reversed_string = string[::-1]
# print("Reversed string:", reversed_string)

#10
#word count
# sentence = input("Enter a sentence: ")
# word_count = len(sentence.split())
# print("Number of words:", word_count)

#11
#digits exist
# string = input("Enter a string: ")
# contains_digit = False
# for char in string:
#     if char.isdigit():
#         contains_digit = True
#         break
# if contains_digit:
#     print("The string contains digits.")
# else:
#     print("The string does not contain any digits.")

#12
#

