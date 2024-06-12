#Task1
'''Write a function that calculates the product of the elements from a list of integers.
The list is passed as a parameter. The result is returned from the function.'''
import math


def amount(numbers):
    return len(numbers)

def task1(numbers):
    product = 1
    for i in numbers:
        product *= i
    return product

list1 = [1, 2, 3, 4]
list2 = [15, 64, 86, 88, 10, 68, 456, 11]
print (f"number of elemetns in list1 is {amount(list1)}")
print (f"number of elemetns in list2 is {amount(list2)}")
print (f"product of list1 is {task1(list1)}")
print (f"product of list2 is {task1(list2)}")

#Task2
'''Write a function to find the minimum in a list of integers. 
The list is passed as a parameter. 
The result is returned from the function.'''

def task2(numbers):
    minimum = min(numbers)
    return minimum

print (f"smallest number from list1 is {task2(list1)}")
print (f"smallest number from list2 is {task2(list2)}")

#Task3
'''Write a function that determines how many prime numbers there are in the list of integers. 
The list is passed as a parameter. The result is returned from the function.'''

def is_prime(n):
    if n <=1:
        return False
    if n <=3:
        return True
    if n > 2 and n % 2 ==0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

def count_primes(numbers):
    count = 0
    for number in numbers:
        if is_prime(number):
            count += 1
    return count
print (f"amount of primes in list1 is {count_primes(list1)}")
print (f"amount of primes in list2 is {count_primes(list2)}")