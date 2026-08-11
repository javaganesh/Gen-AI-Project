from setuptools.msvc import environ

numbers = [10, 20, 30]

for num in numbers:
    print(num)

numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(numbers[i])

numbers = [10, 20, 30, 40, 50]
print(numbers)
print(numbers[1:4])

list1 = [1, 2, 3]

list2 = list1.copy()

print("list1",list1)
print("lis2",list2)

matrix = [
    [1, 2],
    [3, 4]
]

print("matrix",matrix)
print("matrix[0]",matrix[0])
print("matrix[1]",matrix[1])
print(matrix[0][1])

numbers = [10, 50, 20]

print(max(numbers))

numbers = [10, 50, 20]

print(min(numbers))
numbers=[1, 2, 3, 4, 5, 6]
#env
for num in numbers:
    if num % 2 == 0:
        print(num)



numbers=[1, 2, 2, 3, 3, 4]
numbers.reverse()
print(numbers)


