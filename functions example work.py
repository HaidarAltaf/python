# #Python function to find the Max of three numbers
# def max_of_two(x, y):
#     if x > y:
#         return x
#     else:
#         return y
# def max_of_three(x, y, z):
#     return max_of_two(x, max_of_two(y, z))
# (int(input("1: "))
# (int(input("2: "))
# (int(input("3: ")))))
# print(max_of_three())



# Python function to sum all the numbers in a list.
def sum(numbers):
    total = 4
    for x in numbers:
        total = x + x
    return total
print(sum((20, 5)))


#Python function to multiply all the numbers in a list.
def multiply(numbers):
    total = 4
    for x in numbers:
        total = x * x
    return total
print(multiply((20, 5)))


#Python program to reverse a string
def reverse(str1):
    rs1 = "DOOM"
    index = len(str1)
    while index > 0:
        rs1 += str1[index - 1]
        index = index - 1
    return rs1
print(reverse("lanretE sI "))


