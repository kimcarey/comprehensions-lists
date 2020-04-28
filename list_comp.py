numbers = [1,2,3,4,5,6,7,8,9]
# Exercise #1: give me a list with num squared for each num in numbers

new_list = [num*num for num in numbers]
print(new_list)

# Exercise #2: give me a list with num for each num in numbers if num is even
new_list = [num for num in numbers if num % 2 ==0]
print(new_list)

# Exercise #3: I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
new_list = []
for letter in 'spam':
    for num in range(4):
        new_list.append((letter, num))
print(new_list)
