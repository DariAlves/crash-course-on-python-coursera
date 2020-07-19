# 1
for x in range(5):
    print(x)

# 2 
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285

# 3
friends = ['Iori', 'Kyo', 'Terry', 'Joe']
for friend in friends:
    print("Hi, " + friend)

# 4
values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("Total sum: " + str(sum) + " - Average: " + str(sum/length))

# 5
product = 1
for n in range(1, 10):
    product = product * n

print(product)