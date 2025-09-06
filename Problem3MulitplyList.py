# Muhammad Haroon Nasir
# 05/09/25
# Problem 3: A Python function to multiply all the numbers in a list. Uses list [5, 2, 7, -1]

# Function that multiplys all numbers in a given list
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example use
nums = [5, 2, 7, -1]
print(f"The result of multiplying the list is: {multiply_list(nums)}")