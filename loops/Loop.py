# Chat-GPT Exercises about "for" loops.

# # Exercise 1:
# for number in range(1, 6):
#     print(number)

# Exercise 2:
# even_lst = []
# for number in range(11):
#     if number % 2 == 0:
#         even_lst.append(number)
# print(even_lst)

# Exercise 3:
# for number in range(1,6):
#     squared_num = number ** 2
#     print(squared_num)

# Exercise 4:
# total_sum = 0
# for number in range(11):
#     total_sum = total_sum + number
#     print(total_sum)

# Exercise 5:
# for number in range(11):
#     table_5 = number * 5
#     print(f"{number} * 5 = {table_5}")

# Exercise 6:
# num_rows = 6
#
# for num in range(1, num_rows):
#     for j in range(num):
#         print("*", end="")
#     print()

# Exercise 7:
# number = 123
# total_sum = 0
# for digit in str(number):
#     total_sum += int(digit)
# print(f"The sum of the digits is {total_sum}")

# Exercise 7.1:
# number = 456
# total_sum = 0
# for x_num in str(number):
#     total_sum += int(x_num)
# print(f"The sum of the digits is {total_sum}")

# Exercise 8:
# number = 5
# factorial_number = 1
# for x_numb in range(1, number + 1):
#     factorial_number *= x_numb
#     print(f"Factorial number of 5 is: {factorial_number}")

# Exercise 8.1:
# numb = 9
# initial_fact = 1
# for x_numb in range(1, numb + 1):
#     initial_fact *= x_numb
#     print(f"The factorial number of 9 in {x_numb} is: {initial_fact}")

# Exercise 9:
# The Fibonacci Series:
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
#
# iteration_numb = 10
#
# first, second = 0, 1
#
# print(first)
#
# for x_line_iteration in range(2, 11):
#     print(second)
#     first, second = second, first + second


# Exercise 10:
# number_iteration = 20
#
# print(1)
#
# for x_line_iteration in range(2, number_iteration + 1):
#     prime_is = True
#     for y_line_iteration in range(2, x_line_iteration):
#         if x_line_iteration %y_line_iteration == 0:
#             prime_is = False
#             break
#     if prime_is:
#         print(x_line_iteration)

# Exercise 10 repeat
# find the prime in n times of number

# numb_itt = 30
# print(f"Prime is: {int(1)}")
# for x_line in range(2, numb_itt + 1):
#     prime_dime = True
#     for y_line in range(2, x_line):
#         if x_line % y_line == 0:
#             prime_dime = False
#             break
#     if prime_dime:
#         print(f"Prime is: {x_line}")
