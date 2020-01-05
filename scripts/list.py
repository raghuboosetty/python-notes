# arrays in Ruby

# 1D List
numbers = [23, 45, 67, 22]
friends = ["Kevin", "ABC", "def", "Hello", "xyz"]

print(friends[-2])
print(friends[1:])
print(friends[1:3])

friends.extend(numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Kelly")
print(friends)

friends.pop()
print(friends)

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)

numbers.sort()
print(numbers)

print("-------------")
# 2D Lists

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    [0]
]
print(number_grid[0][1])