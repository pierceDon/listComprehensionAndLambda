remainder = lambda num: num % 2

print(remainder(5))

# product = lambda x,y: x * y

# print(product(2,3))

# fruits = [(1, 'peaches'), (2,'bananas'),(3, 'apples'),(4, 'oranges')]
# sorted_fruits = sorted(fruits, key=lambda x: x[1])

# print(sorted_fruits)

# sort dictionary based on price descending

# electronics = {
#     'product1': {'name': 'Laptop', 'price': 800},
#     'product2': {'name': 'Phone', 'price': 1200},
#     'product3': {'name': 'Tablet', 'price': 150},
#     'product4': {'name': 'Monitor', 'price': 300},
# }

# electronics_list = sorted(electronics.items(), key=lambda x:x[1]['price'], reverse=True)
# print(electronics_list)

# numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]

# # display numbers > 7 in ascending order from list above
# filtered_list = list(filter(lambda num: (num > 7), numbers_list))

# print(filtered_list)

#map
result = list(map(lambda x: x % 2, numbers_list))
print(result)

#map with 2 arguments
numbers1 = (1,2,3,4)
numbers2 = (5,6,7,8)

result = list(map(lambda x,y: x + y, numbers1, numbers2))

print(result)