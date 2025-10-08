# friends = ["Matt", "Max" "Martha", "Gloria", "Joy", "Aisha", "Sam"]

# i = 0
# while i < len(friends):
#     print(friends[i])
#     print(i)
# #     i += 1
# friends = ["Matt", "Max", "Martha", "Gloria", "Joy", "Aisha", "Sam"]

# j = len(friends) - 1

# while j >= 0:
#     print(friends[j])
#     j -= 1

# nums = [50, 31, 46, 89, 62, 90, 43, 22, 28, 21]
# even = []
# odd = []

# i =  0
# while i < len(nums):
#     if nums[i] % 2 == 0:
#         even.append(nums[i])
#     else:
#         odd.append(nums[i]) 
#         i+= 1
        
#         print(odd)
#         print(even)

# password = "A234g222222A"

# has_upper = any(p.isupper()for p in password)
# has_lower = any(p.lower()for p in password)
# has_digit = any(p.digit() for p in password)
# has_special = any(not p.isalnum() for p in password)

# if len(password) < 8:
#     strength = "Very Weak"
# elif has_upper and has_lower and has_digit and has_special:
#     strength = "Very strong"
# elif has_upper and has_digit and has_special:
#     strength = "Strong"
# elif has_lower and has_digit:
#     strength = "Medium"
# else:
#     strength = "Weak"

# print(strength)




# num = int(input("enter a number: "))
# for i in range (1,13):
#     print(f"{num} x {i} = {num * i}") 

# num = 3
# for i in range (1,13):
#     print(f"{num} x [i] = {num * i}")


# fruits = ["apple", "mango", "banana", "pawpaw", "watermelon", "grapes", "cherry", "orange", "pineapple", "guava"]
# print(fruits[9])



# students = [("James", 50), ("John", 60), ("Ada", 70), ("Jack", 90)]
# for name, score in students:
#     if score >=90:
#         grade = "A"
#     elif score >=70:
#         grade = "B"
#     elif score >=60:
#         grade = "C"
#     elif score >=50:
#         grade = "D"


# file: beginner_tasks.py

# 1. Password check
# correct_password = "python123"
# while True:
#     password = input("Enter the password: ")
#     if password == correct_password:
#         print("Access granted.")
#         break
#     else:
#         print("Wrong password, try again.")

# print("\n--- Task 2 ---")

# # 2. Take 5 numbers, store in a list, print sum
# numbers = []
# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)
# print("The sum of numbers is:", sum(numbers))

# print("\n--- Task 3 ---")

# # 3. Print even numbers from 2 to 20
# n = 2
# while n <= 20:
#     print(n)
#     n += 2

# print("\n--- Task 4 ---")

# # 4. Guess the number game
# hidden_number = 7
# attempts = 0
# while True:
#     guess = int(input("Guess the number (between 1 and 10): "))
#     attempts += 1
#     if guess == hidden_number:
#         print(f"Correct! It took you {attempts} attempts.")
#         break
#     else:
#         print("Wrong guess, try again.")

# print("\n--- Task 5 ---")

# # 5. Dictionary word meaning lookup
# dictionary = {
#     "python": "A programming language",
#     "apple": "A type of fruit",
#     "car": "A vehicle with four wheels",
#     "book": "A collection of written pages",
#     "school": "A place for learning"
# }

# word = input("Enter a word to look up: ").lower()
# if word in dictionary:
#     print(f"{word}: {dictionary[word]}")
# else:
#     print("Word not found.")
