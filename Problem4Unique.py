# Muhammad Haroon Nasir
# 05/09/25
# Problem 4: Write a Python function that takes a list of numbers and returns a new list with
# unique elements of the first list. Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append function

# Function to create list with unique digits only
def unique_list(numbers):
    unique_nums = []
    for num in numbers:
        # only add if not already present
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

# Example use
nums = [1, 3, 3, 3, 6, 2, 3, 5]
print("Original list:", nums)
print("List with unique elements:", unique_list(nums))