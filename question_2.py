# Assignment - 4

# 2. Write a Python program to triple all numbers of a given list of integers. Use Python map.

size = int(input("Enter the size of list :"))
lst = []

for i in range(size):
    element = int(input("Enter a number :"))
    lst.append(element)

triple_lst = list(map(lambda lst : lst * 3 , lst))

print("Original list :", lst)
print("List after tripling all the elements :", triple_lst)