# Assignment - 4

# 3. Write a Python program to square the elements of a list using map() function.

size = int(input("Enter the size of list :"))
lst = []

for i in range(size):
    element = int(input("Enter a number :"))
    lst.append(element)

square_lst = list(map(lambda lst : lst **2 , lst))

print("Original list :", lst)
print("List after squaring all the elements :", square_lst)