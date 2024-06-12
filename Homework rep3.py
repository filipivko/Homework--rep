#Task5
'''Write a function that takes two lists as a parameter
and returns a list containing the elements of both lists.'''

def combine(l1, l2):
    return l1 + l2
list_a = [1, 2, 3]
list_b = [4, 5, 6]
combined_list = combine(list_a, list_b)
print (combined_list)
#Task6
'''Write a function that calculates the power of each element from the list of integers. 
A value for the power is passed as a parameter, 
the list is also passed as a parameter. The function 
returns a new list containing the results.'''

def powers_of_elements(numbers, power):
    return [number ** power for number in numbers]

list_c =[1, 2, 3, 4, 5]
power_number = 2
result_list = powers_of_elements(list_c, power_number)
print(f"powered list is {result_list}")