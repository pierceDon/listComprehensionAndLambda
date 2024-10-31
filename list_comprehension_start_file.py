'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
new_list = []
for i in original_list:
    if filter(i):
        new_list.append(expressions(i))  '''

#You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in original_list if filter(i)]


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

#There are 3 parts to list comprehension:

#*result*  = [*transform/expression*    *iteration*         *filter*     ]

#The filter part answers the question if the item should be transformed.

x = [i for i in range(10)]
print(x)

#add in an expression (square of all numbers from 1 to 10)

x = [i**2 for i in range(1,11)]
print(x)

#2)

list1 = [3,4,5]
multiplied = [item*3 for item in list1]
print(multiplied)

#3)
listOfWords = ["this","is","a","list","of","words"]
result = [word[0].upper() for word in listOfWords]
print(result)

#4) adding an IF condition
# find the square of all even numbers from 1 to 10
# find the square of all even numbers from 1 to 10
result = [i * i for i in range (1,11) if i % 2 == 0]

# 5)

string = "Hello 12345 World"

# extract all numbers from the string
# output: [1,2,3,4,5]
numbers = [int(x) for x in string if x.isdigit()]

print(numbers)

# extract all letters from the string
# output: "Hello World"
letters = [x for x in string if x.isalpha()]
print(numbers)

words = [x for x in string.split() if x.isalpha()]
print(words)

infile = open('test.txt', 'r')
output = [i.rstrip()for i in infile]

#7
def double(x):
    return x*2

result = [double(x) for x in range(10)]
print(result)

#8 we can use multiple iterables

result = [x+y for x in [10,30,50] for y in [20,40,60] if x > 30 if y > 40]
print(result)


## Exercise ##

# 1 Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]




## 2 create a list of integers which specify the length of each word in
## a sentence except for the word 'the'

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()



## Given dictionary is consisted of vehicles and their weights in kilograms. 
## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
## In the same list comprehension make the key names all upper case.

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110}




## Find all the numbers from 1 to 1000 that have a 4 in them



## count how many times the word 'the' appears in the text file - 'sometext.txt'



## Extract the numbers from the following phrase ##

phrase = 'In 1984 there were 13 instances of a protest with over 1000 people attending. On average there were 15 reported injuries at each event, with about 3 or 4 that were classifled as serious per event.'






