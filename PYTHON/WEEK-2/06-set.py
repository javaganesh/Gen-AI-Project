numbers = {1, 2, 3}
print(numbers)
nums = {1, 2, 3}
print(nums)

nums = {1, 2, 3}

nums.add(4)

print(nums)

nums = {1, 2}

nums.update([3, 4, 5])

print(nums)
nums = {1, 2, 3,4,5,6,7,8,9}
print(nums)

nums.discard(5)
print(nums)

nums = {1, 2, 3}

for num in nums:
    print(num)

nums = {1, 2, 3}

print(2 in nums)

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)

numbers = [1, 2, 2, 3, 3, 4]

unique = list(set(numbers))

print(unique)