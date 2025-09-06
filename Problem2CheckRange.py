# Muhammad Haroon Nasir
# 05/09/25
# Problem 2: A Python function to check whether a number is in a given range 0-9.
# Prints whether the number is in or not in the range

def check_range(n):
    # range(1,10) includes 1–9
    if n in range(1, 10):
        print(n, "is in the range")
    else:
        print(n, "is not in the range")

# Example use
num = int(input("Enter a number: "))
check_range(num)
