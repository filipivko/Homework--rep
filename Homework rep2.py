#task4
'''Write a function that removes a given number from the list of integers.
Return the number of removed elements from the function.'''


def remove(numbers, target, removed_numbers):
    if target in numbers:
        numbers.remove(target)
        removed_numbers.append(target)
    else:
        print(f"{target} not found")
    return

def main():
    list = [1, 2, 3, 4, 5]
    removed = []
    while True:
        print (f"list of numbers: {list}")
        print (f"Removed numbers: {removed}")
        choice = int(input("which number would you like to remove?:"))
        remove(list, choice, removed)

list = [1, 2, 3, 4, 5]
removed = []
if __name__ == "__main__":
    main()