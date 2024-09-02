def find_max(lst):
    # Your code here
    max = 0
    for num in lst:
        if num > max:
            max = num
    return max

# Example usage
print(find_max([3, 7, 2, 9, 5]))  # Output: 9
