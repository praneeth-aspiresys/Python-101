# List of integers
numbers = [1, 2, 3, 4, 5]

fruits = ["apple", "banana", "cherry"]


mixed = [1, "apple", 3.14, True]


nested = [[1, 2], [3, 4], [5, 6]]

print(numbers)
print(fruits)
print(mixed)
print(nested)
fruits.insert(1, "kiwi")
print(fruits)

last_fruit = fruits.pop()
print(last_fruit)
print(fruits)

for idx, fruit in enumerate(fruits):
    print(f"Index {idx}: {fruit}")