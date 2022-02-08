# count = 0
# var1 = str(input("Name: "))

# while count < 5:
#     print(var1, "is useless")
#     count += 1

# countvar = 0
# namelist = []
# while countvar > 5:
#     namelist.append(input("Name: "))
#     countvar = countvar - 1


# countvar = 0
# while countvar < 5:
#     print(namelist[namevar], "is useless")




# Program to make a pattern
# node = 5 
# for i in range(node):
#     for j in range(i):
#         print ('* ', end="")
#     print('')

# for i in range(node, 0, -1):
#     for j in range(i):
#         print('* ', end="")
#     print('')



# Program to reverse words
# var1 = input("word to be reversed: ")
# for char in range(len(var1) - 1, -1, -1):
#     print(var1[char], end="")


# program to count number of even and odd numbers
# var1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# count_odd = 0
# count_even = 0
# for x in var1:
#     if not x % 2:
#         count_even += 1
#     else:
#         count_odd += 1
# print("Even :", count_even)
# print("Odd :", count_odd)



# Program that prints all the numbers from 0 to 6 except 3 and 6.

# for x in range(6):
#     if(x ==3 or x == 6):
#         continue
#     print(x, end=" ")
# print(" ")


# program that write the fibonacci sequence

# x, y = 0, 1
# while y < 150:
#     print(y)
#     x,y = y , (x+y)

#Python program to construct the following pattern, using a nested loop number.

for x in range(15):
    print(str(x) * x)
