# pratical 1 to 13
# uncomment the respective code to run it

# 01 Find Average
sum = 0.0
avg = 0.0
for i in range(1,6):
    sum = sum + float(input(f'Enter the number{i}: '))

avg = sum / 5
print(f'The average is {avg}.')


# 02 Find Odd Even
'''number = int(input(f'Enter the number: '))

if number % 2 == 0:
    print(f'{number} is a even.')
else:
    print(f'{number} is a odd.')'''


# 03 Find Leap Year
'''year = int(input(f'Enter the year: '))

if year%4 == 0 and year%100 !=0 or year%400 ==0:
    print(f'{year} year is a leap year.')
else:
    print(f'{year} year is not a leap year.')'''


# 04 Find Positive Negative 
'''for i in range(3):
    number = int(input(f'Enter the number: '))
    if number < 0:
        print(f'{number} is a negative.')
    elif number == 0:
        print(f'{number} is a zero.')
    else:
        print(f'{number} is a positive.')'''


# 05 Find Greatest Number
'''
number = []
for i in range(1, 3):
    number.append(int(input(f'Enter the number{i}: ')))

if number[0] == number[1]:
    print(f'{number[0]} and {number[1]} are equal.')
elif number[0] > number[1]:
    print(f'{number[0]} is greater than {number[1]}.')
else:
    print(f'{number[1]} is greater than {number[0]}.')
'''

#  06 Find Factorial
'''
number = int(input(f'Enetr the number: '))
fact = 1

if number < 0:
    print(f"Factorial doesn't exists fro negative number.")
elif number == 0:
    print(f'Factorial of 0 is 1.')
else:
    for i in range(1, number+1):
        fact = fact * i
    print(f'Factorial of {number} is a {fact}.')
'''

# 07 Swap Numbers
'''
number = int(input(f'Enetr the number: '))
fact = 1

if number < 0:
    print(f"Factorial doesn't exists fro negative number.")
elif number == 0:
    print(f'Factorial of 0 is 1.')
else:
    for i in range(1, number+1):
        fact = fact * i
    print(f'Factorial of {number} is a {fact}.')
'''

# 08 Find Smallest Number
'''
number = []
for i in range(1, 3):
    number.append(int(input(f'Enter the number{i}: ')))

if number[0] == number[1]:
    print(f'{number[0]} and {number[1]} are equal.')
elif number[0] > number[1]:
    print(f'{number[1]} is smaller than {number[0]}.')
else:
    print(f'{number[0]} is smaller than {number[1]}.')
'''

# 09 Number less than 100
'''
for i in range(3):
    number = int(input(f'Enetr the number: '))
    if number > 100:
        print(f'Number is greater than 100.')
    elif number == 100:
        print(f'Number is a 100.')
    else:
        if number % 2 == 0:
            print(f'Number is less than 100 and even.')
        else:
            print(f'Number is less than 100 and odd.')
'''

# 10 Square Number
'''
for i in range(3):
    number = int(input(f'Enter the number: '))
    if number > 10:
        print(f'Number is not less than 10.')
    elif number == 10:
        print(f'Number is a 10.')
    else:
        print(f'Square of {number} is a {number*number}')
'''

# 11 Find Positive Negative and Zero
'''
for i in range(3):
    number = int(input(f'Enter the number: '))
    if number >= 0:
        if number == 0:
            print(f"{number} is Zero.")
        else:
            print(f"{number} is Positive.")
    else:
        print(f"{number} is Negative.")
'''

# 12 Find greated of 3
'''
number = []
for i in range(1, 4):
    number.append(int(input(f'Enter the number{i}: ')))

if number[0] > number[1]:
    if number[1] > number[2]:
        print(f'{number[0]} is a greatest number.')
    else:
        print(f'{number[2]} is a greatest number.')
elif number[1] > number[0]:
    if number[1] > number[2]:
        print(f'{number[1]} is a greatest number.')
    else:
        print(f'{number[2]} is a greatest number.')
'''

# 13 Find smallest of 3
'''
number = []
for i in range(1, 4):
    number.append(int(input(f'Enter the number{i}: ')))

if number[0] < number[1]:
    if number[1] < number[2]:
        print(f'{number[0]} is a smallest number.')
    else:
        print(f'{number[2]} is a smallest number.')
elif number[1] < number[0]:
    if number[1] < number[2]:
        print(f'{number[1]} is a smallest number.')
    else:
        print(f'{number[2]} is a smallest number.')
'''